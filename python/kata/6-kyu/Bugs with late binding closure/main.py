from solution import create_multiplications
import codewars_test as test

@test.describe("testing for create_multiplications")
def tests():
    @test.it("basic tests")
    def basic_tests():
        res = [m(4) for m in create_multiplications(4)]
        test.assert_equals(res, [0,4,8,12])
        
        res = [m(3) for m in create_multiplications(3)]
        test.assert_equals(res, [0,3,6])
        
        res = [m(0) for m in create_multiplications(0)]
        test.assert_equals(res, [])