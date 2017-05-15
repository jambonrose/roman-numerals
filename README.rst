=======
Read Me
=======

This library will convert integers to unicode Roman numerals, or vice
versa. The library supports `Apostrophus`_ and `Vinculum`_ notation on
top of standard Roman numerals.

This library also supports the use of `unicode fallback characters`_.
For example, when using fallback characters, instead of outputting code
point U+216F (Ⅿ) the library will output the latin M character, which
looks identical to the Roman numeral glyph.

Please keep in mind that fallback characters should only be used if
escape sequences are unavailable.

.. _`Apostrophus`: https://en.wikipedia.org/wiki/Roman_numerals#Apostrophus
.. _`Vinculum`: https://en.wikipedia.org/wiki/Roman_numerals#Vinculum
.. _`unicode fallback characters`: http://www.unicode.org/cldr/charts/31/supplemental/character_fallback_substitutions.html

Road Map
--------

- 0.1 Convert between numerals and integers

- 0.2 Integrate services like PyUp and TravisCI

- 0.3 Add support for fallback characters

- 0.4 Write documenation

- 0.5 Add support for Apostrophus

- 0.6 Add support for Vinculum

- 1.0 Full feature release

Testing
-------

The structure of the project forces tests to run on an installed version
of the code.

You can run the tests directly with `python setup.py test`.
Alternatively, you could install the package with `pip install -e .` or
`python setup.py develop` and then run tests with `py.test`.

To run linters, checkers, and tests on multiple Python versions, simply
invoke `tox`.
