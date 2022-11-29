from geektime_0.precise.core.case_coverage import CaseCoverage
from geektime_0.precise.core.code_diff import CodeDiff
from geektime_0.precise.core.code_line import CodeLine
from geektime_0.precise.tests.test_petclinic import case_coverage


def test_it():
    case_coverage = CaseCoverage()
    case_coverage.load('case_coverage.yaml')

    line1 = CodeLine()
    line1.line_num = 91
    line1.source_file = 'OwnerController.java'
    line1.package = 'org/springframework/samples/petclinic/owner'
    code_diff = CodeDiff()
    code_diff.data = [
        line1
    ]
    r=case_coverage.find_testcases_by_diff(code_diff)
    print(r)
    assert len(r) == 3

    line1 = CodeLine()
    line1.line_num = 99
    line1.source_file = 'OwnerController.java'
    line1.package = 'org/springframework/samples/petclinic/owner'
    code_diff = CodeDiff()
    code_diff.data = [
        line1
    ]
    r = case_coverage.find_testcases_by_diff(code_diff)
    print(r)
    assert len(r) == 1

    line1 = CodeLine()
    line1.line_num = 87
    line1.source_file = 'OwnerController.java'
    line1.package = 'org/springframework/samples/petclinic/owner'
    code_diff = CodeDiff()
    code_diff.data = [
        line1
    ]
    r = case_coverage.find_testcases_by_diff(code_diff)
    print(r)
    assert len(r) == 1
