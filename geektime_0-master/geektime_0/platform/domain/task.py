from dataclasses import dataclass

from geektime_0.platform.db import db


@dataclass
class Task(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(500), nullable=False)
    testcase_id: int = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    testcase = db.relationship("TestCase", back_populates="tasks")
