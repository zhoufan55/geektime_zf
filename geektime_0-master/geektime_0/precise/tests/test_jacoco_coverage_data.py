from geektime_0.precise.jacoco.jacoco_coverage_data import JacocoCoverageData


def test_parse():
    coverage = JacocoCoverageData()
    coverage.parse('./data/test_single.xml')
    print(coverage.lines)
    assert len(coverage.lines) > 0

