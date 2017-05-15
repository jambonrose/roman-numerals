"""Test initial setup.py setup (temporary)"""

from roman_numerals import STANDARD


def test_import():
    """verify that the import worked correctly"""
    assert STANDARD == 1
