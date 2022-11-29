import time

import requests

from geektime_0.app.wework.utils.log import log
from geektime_0.platform.app import app
from geektime_0.platform.db import db

target = 'http://127.0.0.1:5000'


class TestCase:
    def setup_class(self):
        # todo: 数据清理未生效
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_demo(self):
        ...

    def test_post(self):
        r = requests.post(
            target + '/testcase',
            json={
                'name': 'testcase7'
            }
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0

    def test_get(self):
        r = requests.get(
            target + '/testcase/1',
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0
        assert r.json()['data']['name'] == 'testcase2'

    def test_task_get(self):
        r = requests.get(
            target + '/task/1',
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0
        assert r.json()['data']['name'] == 'task1'

    def test_task_post(self):
        r = requests.post(
            target + '/task',
            json={
                'testcase_id': 1
            }
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0

    def test_testcase_task(self):
        r = requests.post(
            target + '/testcase',
            json={
                'name': 'testcase7'
            }
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0
        testcase_id = r.json()['data']

        r = requests.post(
            target + '/task',
            json={
                'testcase_id': testcase_id
            }
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0
