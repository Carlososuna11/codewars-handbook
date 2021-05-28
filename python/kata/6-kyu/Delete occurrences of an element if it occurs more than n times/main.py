import codewars_test as test
from solution import delete_nth

test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])