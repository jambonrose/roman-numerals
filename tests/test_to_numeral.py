"""
Test conversion from integer to Roman numeral
"""
import pytest

from roman_numerals import LOWERCASE, convert_to_numeral

from .parameters import LOWERCASE_PARAMETERS, STANDARD_PARAMETERS


@pytest.mark.parametrize(
    "decimal_integer, expected_numeral",
    STANDARD_PARAMETERS)
def test_standard_numeral_conversion(
        decimal_integer: int, expected_numeral: str,
) -> None:
    """
    Test conversion from integers to uppercase Unicode Roman numerals
    """
    assert convert_to_numeral(decimal_integer) == expected_numeral


@pytest.mark.parametrize(
    "decimal_integer, expected_numeral",
    LOWERCASE_PARAMETERS)
def test_lowercase_numeral_conversion(
        decimal_integer: int, expected_numeral: str,
) -> None:
    """
    Test conversion from integers to lowercase Unicode Roman numerals
    """
    assert (
        convert_to_numeral(decimal_integer, mode=LOWERCASE) == expected_numeral
    )
