import codewars_test as test
from solution import validBraces

test.assert_equals(validBraces("()"), True);
test.assert_equals(validBraces("[(])"), False);