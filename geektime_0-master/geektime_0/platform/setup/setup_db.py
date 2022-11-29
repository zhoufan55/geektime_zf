from sqlalchemy.orm import Query

from geektime_0.platform.app import app
from geektime_0.platform.db import db
# 需要保留以保证sqlalchemy可以发现对应的数据库类
from geektime_0.platform.domain import *
from geektime_0.platform.domain.user import User

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        # user = User.query.filter(User.username == 'u2').first()
        # print(user)
        # all = User.query.filter(User.username != '').all()
        # print(all)
