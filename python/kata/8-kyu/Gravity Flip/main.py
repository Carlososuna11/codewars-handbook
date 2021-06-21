import codewars_test as test
from solution import flip
@test.describe("Sample tests")
def sample_tests():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(flip('R', [3, 2, 1, 2]), [1, 2, 2, 3])
    @test.it("Test 2")
    def test_2():
        test.assert_equals(flip('L', [1, 4, 5, 3, 5]), [5, 5, 4, 3, 1])
