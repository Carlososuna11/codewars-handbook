import codewars_test as test
from solution import Calculator
@test.describe("Sample tests")
def sample_tests():
    test.assert_equals(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
    test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
    test.assert_equals(Calculator().evaluate('1 + 1'), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
    test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
    test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)