from geektime_0.platform.jenkins import jenkins


def test_jenkins():
    jenkins['demo'].invoke(build_params={'nodeid': 'xxx.py:XXX:test_method'})