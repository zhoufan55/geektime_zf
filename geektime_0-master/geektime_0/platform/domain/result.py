from geektime_0.platform.db import db


class Result(db.model):
    # 代表的是一组测试用例，可以设置套件的setup teardown 执行流程 并行 串行 套件组合
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.String(1000))
