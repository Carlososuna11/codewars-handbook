import codewars_test as test
from solution import decodeMorse
def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
        test.expect(False)

test.describe("Example from description")
test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

test.describe("Your own tests")
# Add more tests here