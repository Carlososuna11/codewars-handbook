import codewars_test as test
from solution import driver
@test.describe('Example Tests')

def example_tests():
    data = ["John", "James", "Smith", "01-Jan-2000", "M"]
    @test.it("Should return SMITH001010JJ9AA")
    def example_test_case():
        test.assert_equals(driver(data), "SMITH001010JJ9AA")
    
    data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
    @test.it("Should return GIBBS862131J99AA")
    def example_test_case():
        test.assert_equals(driver(data), "GIBBS862131J99AA")
    
    data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
    @test.it("Should return LEE99809021AR9AA")
    def example_test_case():
        test.assert_equals(driver(data), "LEE99809021AR9AA")