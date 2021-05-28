import codewars_test as test
from solution import valid_parentheses

test.assert_equals(valid_parentheses("  ("),False)
test.assert_equals(valid_parentheses(")test"),False)
test.assert_equals(valid_parentheses(""),True)
test.assert_equals(valid_parentheses("hi())("),False)
test.assert_equals(valid_parentheses("hi(hi)()"),True)