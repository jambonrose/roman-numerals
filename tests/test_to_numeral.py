"""
Test conversion from integer to Roman numeral
"""
from typing import Any

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


@pytest.mark.parametrize("non_integer_values", [
    'hello',
    1.0,
    True,
    set(),
    {'hello': 5},
])
def test_invalid_types(non_integer_values: Any) -> None:
    """
    Ensure that passing in non-integers results in Type exceptions
    """
    with pytest.raises(TypeError):
        convert_to_numeral(non_integer_values)


@pytest.mark.parametrize("invalid_mode_values", [
    'moo',
    True,
    False,
    1000,
    -5,
    19.04,
    set([1, 2, 3]),
    {'hi': 'there'},
])
def test_invalid_mode_values(invalid_mode_values: Any) -> None:
    """
    Ensure that passing in non-integers results in Type exceptions
    """
    with pytest.raises(ValueError):
        convert_to_numeral(10, mode=invalid_mode_values)
