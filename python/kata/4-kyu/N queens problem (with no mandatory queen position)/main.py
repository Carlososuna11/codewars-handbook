import codewars_test as test
from solution import nQueen

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("N=1")
    def test_1():
        test.assert_equals(nQueen(1), [0]);
    
    @test.it("N=2")
    def test_2():
        test.assert_equals(nQueen(2), [ ]);
    
    @test.it("N=3")
    def test_3():
        test.assert_equals(nQueen(3), [ ]);
    
    @test.it("N=8")
    def test_8():
        solution = nQueen(8)
        test.expect(sample_check(8, solution), f"{solution} is invalid" );
        