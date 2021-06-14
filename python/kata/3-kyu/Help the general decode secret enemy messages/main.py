import codewars_test as test

@test.describe("Sample Test")
def test_group():
    @test.it("Should be compatible with encoder")
    def test_case():
        test.assert_equals(decode(encode("Hello World!")), "Hello World!")
    @test.it("Should crack encoded message")
    def test_case2():
        test.assert_equals(decode("atC5kcOuKAr!"), "Hello World!")