import intro

class TestCalculator:
    def test_addition(self):
        assert 4 == intro.add(2,2)
    def test_subtraction(self):
        assert 0 == intro.subtract(5,5)