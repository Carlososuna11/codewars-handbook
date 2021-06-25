import codewars_test as test
from solution import t_area
@test.describe('Basic tests.')
def triangle_tests():

    @test.it('First triangle area')
    def test_case1():
        test.assert_equals(t_area('\n.\n. .\n'), .5) 
        
    @test.it('Second triangle area')
    def test_case2():
        test.assert_equals(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n'),8.0)
                           
    @test.it('Third triangle area')
    def test_case3():
        test.assert_equals(t_area('\n.\n. .\n. . .\n'), 2.0) 

    @test.it('Forth triangle area')
    def test_case4():
        test.assert_equals(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n'), 32.0) 
