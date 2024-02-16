# Test Cases (test_reverse_string.py)

import functions


def test_string_reversal():
    assert functions.reverse_string("hello") == "olleh"
    # for empty string
    assert functions.reverse_string("") == ""


def test_leap_years():
    assert (functions.is_leap_year(2020))
    assert (functions.is_leap_year(2000))
    assert (functions.is_leap_year(2400))


def test_non_leap_years():
    assert not (functions.is_leap_year(2021))
    assert not(functions.is_leap_year(1900))
    assert not (functions.is_leap_year(2000))

