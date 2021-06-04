import codewars_test as test
import timeit
from solution import alphametics

test.describe('Example Tests')
example_tests = (
	('SEND + MORE == MONEY','9567 + 1085 = 10652'),# 0..9: 0.4 / 0..5,9..6
	('ZEROES + ONES == BINARY','698392 + 3192 = 701584'),# 0..9: 9.7 / 0..5,9..6
	('COUPLE + COUPLE == QUARTET','653924 + 653924 = 1307848'),# 0..9: 8.7 / 0..5,9..6
	('DO + YOU + FEEL == LUCKY','57 + 870 + 9441 = 10368'),# 0..9: 5.80 / 0..5,9..6
	('ELEVEN + NINE + FIVE + FIVE == THIRTY','797275 + 5057 + 4027 + 4027 = 810386'),# 0..9:4.97 / 0..5,9..6
    # ('GQRAOO + COGPY + RKYKPPC + CACRK + GGAOOCHY + ORHRKYHP + CCHYRCGG = QPQAYOHPA','823755 + 65814 + 3949116 + 67639 + 88755604 + 53039401 + 66043688 = 212745017'),
)
starttime = timeit.default_timer()
for inp,out in example_tests:
    assertime =timeit.default_timer() 
    test.assert_equals(alphametics(inp),out)
    print("assert time", timeit.default_timer() - assertime)
print("\nTOTAL TIME", timeit.default_timer() - starttime)