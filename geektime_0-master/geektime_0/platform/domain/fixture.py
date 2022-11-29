from geektime_0.platform.db import db


class Fixture(db.model):
    # 代表的是配置 环境数据 测试数据
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.String(1000))
