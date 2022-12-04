import requests

from geektime_0.app.wework.utils.log import log
from geektime_0.platform.app import app
from geektime_0.platform.db import db

target = 'http://192.168.1.14:5001'


def test_testcase():
    r = requests.post(
        target + '/testcase',
        json={
            'batch': 1,
            'git': 'https://github.com/zhoufan55/geektime_zf.git'
        }
    )
    log.debug(r.text)


if __name__ == '__main__':
    test_testcase()
