import pytest
from math_utils import calculate_discount, calculate_total_with_tax


def test_calculate_discount_valid():
    # $100 item with 20% discount should give $20.0 discount
    assert calculate_discount(100.0, 20.0) == 20.0


def test_calculate_discount_zero():
    assert calculate_discount(100.0, 0.0) == 0.0


def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError):
        calculate_discount(100.0, 150.0)


def test_calculate_discount_negative_percent():
    with pytest.raises(ValueError):
        calculate_discount(100.0, -10.0)


def test_calculate_total_with_tax():
    assert calculate_total_with_tax(100.0, 0.10) == 110.0
