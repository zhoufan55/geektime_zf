from dataclasses import dataclass

from geektime_0.platform.db import db


@dataclass
class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(100), unique=True, nullable=False)
    email: str = db.Column(db.String(100))
    password: str = db.Column(db.String(100))
