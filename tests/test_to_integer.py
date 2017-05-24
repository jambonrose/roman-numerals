"""
Test conversion from integer to Roman numeral
"""
import pytest

from roman_numerals import convert_to_integer

from .parameters import LOWERCASE_PARAMETERS, STANDARD_PARAMETERS


@pytest.mark.parametrize(
    "expected_integer, roman_numeral",
    LOWERCASE_PARAMETERS + STANDARD_PARAMETERS)
def test_integer_conversion(
        roman_numeral: str, expected_integer: int,
) -> None:
    """
    Test conversion from integers to uppercase Unicode Roman numerals
    """
    assert convert_to_integer(roman_numeral) == expected_integer
