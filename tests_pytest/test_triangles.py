import pytest
from tests.test_function import triangle_are


class TestTrianglePositive:
    @pytest.mark.positive
    def test_triangle_5_4_3(self):
        assert triangle_are(5, 4, 3) == 6.0

    @pytest.mark.negative
    def test_triangle_2_2_2_case1(self):
        assert triangle_are(2, 2, 2) == 2.0

    @pytest.mark.negative
    def test_triangle_3_2_2(self):
        assert triangle_are(3, 2, 2) == 2.0

    @pytest.mark.prime
    @pytest.mark.xfail
    def test_triangle_4_2_2(self):
        assert triangle_are(4, 2, 2) == 2.0


def polindrom(text):
    input_text = input('Enter your word: ')
    if input_text == input_text[::-1]:
        return True
    else:
        return False


