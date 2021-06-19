import codewars_test as test
from solution import type_of_triangle

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(type_of_triangle(1,1,1), "Equilateral")
        test.assert_equals(type_of_triangle(3,2,4), "Scalene")
        test.assert_equals(type_of_triangle(2,2,1), "Isosceles")
        test.assert_equals(type_of_triangle('.',5,82), "Not a valid triangle")