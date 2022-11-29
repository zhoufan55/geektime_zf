from dataclasses import dataclass

from geektime_0.platform.db import db
from geektime_0.platform.domain.task import Task


@dataclass
class TestCase(db.Model):
    #业务测试用例 po模式 业务模型 + 自动化模型
    # admin.login(name pw); admin.add_product(img name) robotframework calabash
    # sendkeys click find  selenium appium
    # nodeid
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True, nullable=False)
    tasks: Task = db.relationship("Task", back_populates="testcase")
    data: str = db.Column(db.String(1000))
    # data = db.Column(db.String(1000))  数据驱动 在线编辑 没有版本管理
    # nodeid =  db.Column(db.String(100))  通用大部分测试框架 用例编号与用例的定义解耦，可以充分的使用git
