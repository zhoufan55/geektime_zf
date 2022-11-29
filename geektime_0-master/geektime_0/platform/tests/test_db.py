from sqlalchemy.orm import Query

from geektime_0.app.wework.utils.log import log
from geektime_0.platform.app import app
from geektime_0.platform.db import db
from geektime_0.platform.domain.task import Task
from geektime_0.platform.domain.testcase import TestCase


def test_init():
    with app.app_context():
        db.drop_all()
        db.create_all()

        log.debug(db.session.execute(db.select(TestCase)).scalars().all())

        testcase = TestCase()
        testcase.name = 'testcase1'

        task = Task(name='task1')
        task.testcase = testcase

        db.session.add(task)
        db.session.add(testcase)

        db.session.commit()

        log.debug(db.session.execute(db.select(TestCase)).scalars().all())

        query: Query = TestCase.query
        testcase = TestCase.query.first()
        log.debug(testcase)
        log.debug(testcase.tasks)
