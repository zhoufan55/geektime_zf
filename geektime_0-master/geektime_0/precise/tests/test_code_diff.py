from geektime_0.precise.core.code_diff import CodeDiff


def test_load():
    diff=CodeDiff()
    diff.load('/Users/seveniruby/projects/spring-petclinic', 'main', 'geektime')

