from geektime_0.platform.db import db


class Runner(db.model):
    # 代表的是用例执行引擎  jmeter pytest junit HttpRunner RobotFramework
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.String(1000))
