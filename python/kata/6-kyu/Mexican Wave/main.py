import codewars_test as test
from solution import wave

@test.describe('Example Tests')

def example_tests():
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case1():
        test.assert_equals(wave("hello"), result)
    
    result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case2():
        test.assert_equals(wave("codewars"), result)
    
    result = []
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case3():
        test.assert_equals(wave(""), result)
    
    result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case4():
        test.assert_equals(wave("two words"),result)
    
    result = [" Gap ", " gAp ", " gaP "]
    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case5():
        test.assert_equals(wave(" gap "), result)