from geektime_0.precise.core.coverage_agent import CoverageAgent
from geektime_0.precise.jacoco.jacoco_coverage_agent import JacocoCoverageAgent


def test_collect():
    agent = JacocoCoverageAgent(
        home='/Users/seveniruby/ke/shift_left/jacoco/latest',
        project='/Users/seveniruby/projects/spring-petclinic',
        host='127.0.0.1',
        port=6300
    )
    agent.clear()
    path=agent.collect('/tmp/jacoco')
    assert path == '/tmp/jacoco/jacoco.xml'
