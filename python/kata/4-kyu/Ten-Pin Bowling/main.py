import codewars_test as test
from solution import bowling_score

test.describe('Basic Tests')
test.it('maybe this bowler should put bumpers on')
test.assert_equals(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
test.it('woah! Perfect game!')
test.assert_equals(bowling_score('X X X X X X X X X XXX'), 300)
test.assert_equals(bowling_score('20 40 05 31 27 8/ 23 9/ X XX1'), 112)
test.assert_equals(bowling_score('8/ 52 X 34 X 08 8/ 8/ 32 1/X'), 128)