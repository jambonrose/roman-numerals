"""
Library to convert to and from Roman numerals in various encodings
"""

from re import match, sub as substitute

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
    ('ⅤⅠⅠⅠ', 'Ⅷ'),
    ('ⅤⅠⅠ', 'Ⅶ'),
    ('ⅤⅠ', 'Ⅵ'),
    ('ⅠⅠⅠ', 'Ⅲ'),
    ('ⅠⅠ', 'Ⅱ'),
]

STANDARD_TRANS = 'ⅯⅮⅭⅬⅫⅪⅩⅨⅧⅦⅥⅤⅣⅢⅡⅠ'
LOWERCASE_TRANS = 'ⅿⅾⅽⅼⅻⅺⅹⅸⅷⅶⅵⅴⅳⅲⅱⅰ'


def convert_to_numeral(decimal_integer: int, mode: int = STANDARD) -> str:
    """Convert a decimal integer to a Roman numeral"""
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


def convert_to_integer(roman_numeral: str) -> int:
    """Convert a Roman numeral to a decimal integer"""
    return_value = 0
    partial_numeral = roman_numeral

    for full_string, shortening in SHORTENINGS:
        partial_numeral = substitute(
            r'%s$' % shortening,
            full_string,
            partial_numeral,
        )

    for integer, numeral in ROMAN_NUMERAL_TABLE:
        pattern_match = match(r'^(%s)*' % numeral, partial_numeral)
        if pattern_match:
            chars_matched = len(pattern_match.group())
            numerals_matched = chars_matched // len(numeral)
            return_value += numerals_matched * integer
            partial_numeral = partial_numeral[chars_matched:]
    return return_value
