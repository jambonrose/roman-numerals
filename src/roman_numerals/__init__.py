"""
Library to convert to and from Roman numerals in various encodings
"""

from re import (
    VERBOSE, compile as re_compile, fullmatch, match, sub as substitute,)

# Operation Modes
STANDARD = 1
LOWERCASE = 2

ROMAN_NUMERAL_TABLE = [
    (1000, 'Ⅿ'),
    (900, 'ⅭⅯ'),
    (500, 'Ⅾ'),
    (400, 'ⅭⅮ'),
    (100, 'Ⅽ'),
    (90, 'ⅩⅭ'),
    (50, 'Ⅼ'),
    (40, 'ⅩⅬ'),
    (10, 'Ⅹ'),
    (9, 'Ⅸ'),
    (5, 'Ⅴ'),
    (4, 'Ⅳ'),
    (1, 'Ⅰ'),
]

SHORTENINGS = [
    ('ⅩⅠⅠ', 'Ⅻ'),
    ('ⅩⅠ', 'Ⅺ'),
    ('ⅠⅩ', 'Ⅸ'),
    ('ⅤⅠⅠⅠ', 'Ⅷ'),
    ('ⅤⅠⅠ', 'Ⅶ'),
    ('ⅤⅠ', 'Ⅵ'),
    ('ⅠⅤ', 'Ⅳ'),
    ('ⅠⅠⅠ', 'Ⅲ'),
    ('ⅠⅠ', 'Ⅱ'),
]
STANDARD_TRANS = 'ⅯⅮⅭⅬⅫⅪⅩⅨⅧⅦⅥⅤⅣⅢⅡⅠ'
LOWERCASE_TRANS = 'ⅿⅾⅽⅼⅻⅺⅹⅸⅷⅶⅵⅴⅳⅲⅱⅰ'


def convert_to_numeral(decimal_integer: int, mode: int = STANDARD) -> str:
    """Convert a decimal integer to a Roman numeral"""
    if (not isinstance(decimal_integer, int)
            or isinstance(decimal_integer, bool)):
        raise TypeError("decimal_integer must be of type int")
    if (not isinstance(mode, int)
            or isinstance(mode, bool)
            or mode not in [LOWERCASE, STANDARD]):
        raise ValueError(
            "mode must be "
            "roman_numerals.STANDARD "
            "or roman_numerals.LOWERCASE "
        )
    return_list = []
    remainder = decimal_integer
    for integer, numeral in ROMAN_NUMERAL_TABLE:
        repetitions, remainder = divmod(remainder, integer)
        return_list.append(numeral * repetitions)
    numeral_string = ''.join(return_list)

    for full_string, shortening in SHORTENINGS:
        numeral_string = substitute(
            r'%s$' % full_string,
            shortening,
            numeral_string,
        )

    if mode == LOWERCASE:
        trans_to_lowercase = str.maketrans(STANDARD_TRANS, LOWERCASE_TRANS)
        numeral_string = numeral_string.translate(trans_to_lowercase)
    return numeral_string


NUMERAL_PATTERN = re_compile(
    """
    Ⅿ*                # thousands
    (ⅭⅯ|ⅭⅮ|Ⅾ?Ⅽ{0,3})  # hundreds - ⅭⅯ (900), ⅭⅮ (400), ⅮⅭⅭⅭ (800), ⅭⅭⅭ (300)
    (ⅩⅭ|ⅩⅬ|Ⅼ?Ⅹ{0,3})  # tens - ⅩⅭ (90), ⅩⅬ (40), ⅬⅩⅩⅩ (80), ⅩⅩⅩ (30)
    (Ⅸ|Ⅳ|Ⅴ?Ⅰ{0,3})   # ones - Ⅸ (9), Ⅳ (4), ⅤⅠⅠⅠ (8), ⅠⅠⅠ (3)
    """,
    VERBOSE
)


def convert_to_integer(roman_numeral: str) -> int:
    """Convert a Roman numeral to a decimal integer"""
    if not isinstance(roman_numeral, str):
        raise TypeError("decimal_integer must be of type int")
    if roman_numeral == '':
        raise ValueError("roman_numeral cannot be an empty string")

    # ensure all characters are in the standard/uppercase set
    trans_to_uppercase = str.maketrans(LOWERCASE_TRANS, STANDARD_TRANS)
    # named partial_numeral because it will be shortened in loop below
    partial_numeral = roman_numeral.translate(trans_to_uppercase)

    # remove Unicode shortenings in favor of chars in conversion table
    for full_string, shortening in SHORTENINGS:
        partial_numeral = substitute(
            r'%s$' % shortening,
            full_string,
            partial_numeral,
        )

    if not fullmatch(NUMERAL_PATTERN, partial_numeral):
        raise ValueError(
            "the string %s is not a valid numeral" % roman_numeral
        )

    # convert uppercase roman numerals to integer
    return_value = 0
    for integer, numeral in ROMAN_NUMERAL_TABLE:
        pattern_match = match(r'^(%s)+' % numeral, partial_numeral)
        if pattern_match:
            chars_matched = len(pattern_match.group())
            numerals_matched = chars_matched // len(numeral)
            return_value += numerals_matched * integer
            partial_numeral = partial_numeral[chars_matched:]
    return return_value


def undo_shortenings(value):
  for full_string, shortening in SHORTENINGS:
    value = value.replace(shortening, full_string)
  return value


def roman_to_ascii(value):
  value = undo_shortenings(value=value)
  return value.replace("Ⅰ", "I").replace("Ⅴ", "V").replace("Ⅹ", "X").replace("Ⅼ", "L").replace("Ⅽ", "C").replace("Ⅾ", "D").replace("Ⅿ", "M")
