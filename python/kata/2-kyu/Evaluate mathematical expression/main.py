import codewars_test as Test
from solution import calc

tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14],
    ["2 + 3 * 4 / 3 - 6 / 3 * 3 + 8",8],
    ["(2 / (2 + 3.33) * 4) - -6",7.5],
    ['1-1',0],
    ['-67 / -32 - -43 + 43 / -73 / -37 * -20 - 58', -13.224650592373195],
    ['79 * 9 - -96 * 54 + -80 + -70 * 27 + -69',3856]
]

for test in tests:
    Test.assert_equals(calc(test[0]), test[1])