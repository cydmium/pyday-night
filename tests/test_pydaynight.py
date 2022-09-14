import datetime

import pytest

import pydaynight


def test_julian_day():
    assert (
        round(pydaynight.julian_day(datetime.datetime(2000, 1, 1, 12, 30, 30)), 9)
        == 2.451545021180556e6
    )  # Normal Conditions
    assert (
        pydaynight.julian_day(datetime.datetime(1, 1, 1)) == 1721425.5
    )  # Edge of date range
    assert pydaynight.julian_day(datetime.datetime(2000, 1, 1)) == 2451544.5  # Day Only
    assert (
        pydaynight.julian_day(datetime.datetime(2000, 1, 1, 12)) == 2451545
    )  # Int-like output
