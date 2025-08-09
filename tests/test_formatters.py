import pytest

from freqtrade.util.formatters import strip_trailing_zeros


def test_strip_trailing_zeros_basic():
    assert strip_trailing_zeros("1.2300") == "1.23"
    assert strip_trailing_zeros("1.000") == "1"


def test_strip_trailing_zeros_zero_value():
    assert strip_trailing_zeros("0.000") == "0"
    assert strip_trailing_zeros("0") == "0"
    assert strip_trailing_zeros("-0.000") == "0"
