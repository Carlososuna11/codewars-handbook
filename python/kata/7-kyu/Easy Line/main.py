import codewars_test as test
from solution import easyline

def testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("easyline")
test.it("Basic tests")
testing(easyline(7), 3432)
testing(easyline(13), 10400600)
testing(easyline(17), 2333606220)
testing(easyline(19), 35345263800)