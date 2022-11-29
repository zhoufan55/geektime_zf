from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

from geektime_0.platform.app import app

db = SQLAlchemy()
db.init_app(app)
