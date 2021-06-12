import codewars_test as test
from solution import solve_n_queens

@test.describe("N Queens Test")
def test_group():
    @test.describe("Basic Tests")
    def test_basic():
        test_cases = [
            {'size': 1, 'fixed': (0, 0), 'solution': 'Q\n'},
            {'size': 4, 'fixed': (0, 2), 'solution': '..Q.\nQ...\n...Q\n.Q..\n'},
            {'size': 6, 'fixed': (1, 2), 'solution': '....Q.\n..Q...\nQ.....\n.....Q\n...Q..\n.Q....\n'},
        ]
        for test_case in test_cases:
            size = test_case['size']
            fixed = test_case['fixed']
            solution = test_case['solution']
            
            @test.it(f'Testing size={size}, fixed=({fixed})')
            def test_it():
                test.assert_equals(solve_n_queens(size, fixed), solution)
                
    @test.describe('No Solution')
    def test_no_solution():
        test_cases = [
            [2, (0, 0)],
            [3, (0, 2)],
            [4, (2, 1)],
            [6, (2, 3)]
        ]
        
        for test_case in test_cases:
            size = test_case[0]
            fixed = test_case[1]
            
            @test.it(f'Testing size={size}, fixed={fixed}')
            def test_it():
                test.assert_equals(solve_n_queens(size, fixed), None)