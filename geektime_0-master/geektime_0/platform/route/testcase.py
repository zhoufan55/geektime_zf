from dataclasses import asdict

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm import Query

from geektime_0.platform.app import app
from geektime_0.platform.db import db
from geektime_0.platform.domain.testcase import TestCase
from geektime_0.platform.jenkins import jenkins

testcase_bp = Blueprint('testcase', __name__)


@testcase_bp.route('/testcase/<id>', methods=['GET'])
@jwt_required()
def case_get_id(id):
    # testcase=db.session.execute(db.select(TestCase)).scalars().first()
    testcase = TestCase.query.filter(TestCase.id == id).first()
    tasks = [asdict(task) for task in testcase.tasks]

    return {
        'errcode': 0,
        'data': asdict(testcase),
        'tasks': tasks
    }


@testcase_bp.route('/testcase', methods=['GET'])
def case_get():
    testcases = [asdict(item) for item in TestCase.query.all()]
    return {
        'errcode': 0,
        'data': testcases
    }


@testcase_bp.route('/testcase', methods=['POST'])
def case_post():
    # 等待jenkins分析完测试结果并回传测试用例
    if request.args.get('batch'):
        # 批量上传测试用例
        # 去重判断
        git = request.args.get('git')
        app.logger.info(git)
        app.logger.info(request.data)
        testcase_list = request.json
        for item in testcase_list:
            testcase = TestCase(**item)
            testcase.data = git
            db.session.add(testcase)
            app.logger.info(testcase)
        testcase_id = None
    else:
        # 单个上传测试用例
        testcase = TestCase()
        testcase.name = request.json['name']
        db.session.add(testcase)
        testcase_id = testcase.id
    db.session.commit()
    return {
        'errcode': 0,
        'data': testcase_id
    }


@testcase_bp.route('/testcase', methods=['PUT'])
# @jwt_required()
def testcase_import():
    # 启动jenkins去实现代码的下载和测试用例的分析，并批量回传测试用例
    git = request.args.get('git', None)
    if git:
        jenkins['testcase_import'].invoke(build_params={'git': git})
        return jsonify(errcode=0)
    else:
        return jsonify(errcode=1)
