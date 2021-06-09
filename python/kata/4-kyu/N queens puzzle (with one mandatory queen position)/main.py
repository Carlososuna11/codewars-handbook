import codewars_test as test
from solution import queens
@test.describe("Sample tests")
def sample_tests():
  
  @test.it("Size=1")
  def test_n_1():
      test.expect(check_solution_valid(queens("a1", 1), "a1", 1))
      
  @test.it("Size=4")
  def test_n_4():
      test.expect(check_solution_valid(queens("b4", 4), "b4", 4))
      
  @test.it("Size=8")
  def test_n_8():
      test.expect(check_solution_valid(queens("c7", 8), "c7", 8))