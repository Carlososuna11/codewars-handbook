import codewars_test as test
from solution import increment_string

test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string(""), "1")