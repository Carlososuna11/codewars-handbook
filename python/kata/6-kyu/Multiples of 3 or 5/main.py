import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should handle basic cases")
    def basic_tests():
        test.assert_equals(solution(10), 23)
   