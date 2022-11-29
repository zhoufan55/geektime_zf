import json
from dataclasses import asdict

from flask import Blueprint, render_template, request, jsonify, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, set_access_cookies
from sqlalchemy.orm import Query

from geektime_0.platform.app import app
from geektime_0.platform.db import db
from geektime_0.platform.domain.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return render_template('hello.html', Ïargs=request.args)


@auth_bp.route('/login.html', methods=['GET'])
def login_html():
    return render_template('login.html', args=request.args)


@auth_bp.route('/login.json', methods=['POST', 'GET'])
def login():
    data = request.args or request.json
    user = User(**data)
    r = User.query.filter(User.username == user.username, User.password == user.password).first()
    if r:
        # 生成用户相关的token
        access_token = create_access_token(r.username)
        res = jsonify(errcode=0, data=asdict(r), token=access_token)
        # 保存token到cookie
        set_access_cookies(res, access_token)
        return res
    else:
        return jsonify(errcode=1, msg=f'no such {user}')


@auth_bp.route('/profile.json', methods=['POST', 'GET'])
@jwt_required()
def profile():
    username = get_jwt_identity()
    return jsonify(errcode=0, data=username)


@auth_bp.route('/registry', methods=['POST', 'GET'])
def register():
    user = User(**request.args)
    db.session.add(user)
    db.session.commit()
    return jsonify(errcode=0, data=user)


@auth_bp.route('/users/<id>')
def users(id):
    # users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    # app.logger.error(users)

    app.logger.info(User.query.get(id).username)
    app.logger.info(User.query.all()[0].username)
    result = db.session.execute(db.select(User)).first()
    app.logger.info(result[0].email)
    users = db.session.execute(db.select(User).order_by(User.username)).scalars().all()
    app.logger.info(users)
    return users
