import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 7, 5) == 35

    def test_division_correct(self):
        assert self.calc.division(self, 144, 12) == 12

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 29, 11) == 18

    def test_adding_correct(self):
        assert self.calc.adding(self, 13, 20) == 33