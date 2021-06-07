import codewars_test as test
from solution import corner_fill

test_cases = [
    ('1x1 square',
     [[1]],      [1]
    ),
    ('2x2 square',
     [[1,2],
      [4,5]],    [1, 2, 5, 4]
    ),
    ('3x3 square',
     [[1,2,3],
      [4,5,6],
      [7,8,9]],  [1, 2, 3, 6, 9, 8, 5, 4, 7]
    ),
]

@test.describe('Sample tests')
def sample_tests():
    for name, square, expected in test_cases:
        @test.it(name)
        def _():
            test.assert_equals(corner_fill(square), expected)