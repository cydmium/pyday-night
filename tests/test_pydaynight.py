import datetime

import numpy as np
import pytest

import pydaynight


def test_julian_day():
    # Normal Conditions
    assert (
        round(pydaynight.julian_day(datetime.datetime(2000, 1, 1, 12, 30, 30)), 9)
        == 2.451545021180556e6
    )
    # Edge of date range
    assert pydaynight.julian_day(datetime.datetime(1, 1, 1)) == 1721425.5
    # Day Only
    assert pydaynight.julian_day(datetime.datetime(2000, 1, 1)) == 2451544.5
    # Int-like output
    assert pydaynight.julian_day(datetime.datetime(2000, 1, 1, 12)) == 2451545
    # Leap Years
    assert (
        round(pydaynight.julian_day(datetime.datetime(2004, 2, 29, 3, 42, 13)), 9)
        == 2.453064654317129e6
    )


def test_sun_angle_no_elevation():
    # Mid-day at equator & prime meridian on Jan 1, 2000 12 UT
    assert (
        round(pydaynight.sun_angle(datetime.datetime(2000, 1, 1, 12), 0, 0), 4)
        == 66.9519
    )

    # Nighttime at 30, 30 on Jan 1, 1900
    assert (
        round(pydaynight.sun_angle(datetime.datetime(1900, 1, 1), 30, 30), 4)
        == -63.1021
    )


def test_sun_angle_with_elevation():
    # Mid-day at equator & prime meridian on Jan 1, 2000 12 UT at 60 km
    assert (
        round(pydaynight.sun_angle(datetime.datetime(2000, 1, 1, 12), 0, 0, 60), 4)
        == 74.7852
    )

    # Nighttime at 30, 30 on Jan 1, 1900 at 60 km
    assert (
        round(pydaynight.sun_angle(datetime.datetime(1900, 1, 1), 30, 30, 60), 4)
        == -55.2687
    )

    # Mid-day at equator & prime meridian on Jan 1, 2000 12 UT at 80 km
    assert (
        round(
            pydaynight.sun_angle(datetime.datetime(2000, 1, 1, 12, 0, 0), 0, 0, 80), 4
        )
        == 75.9853
    )

    # Nighttime at 30, 30 on Jan 1, 1900 at 80 km
    assert (
        round(
            pydaynight.sun_angle(datetime.datetime(1900, 1, 1, 0, 0, 0), 30, 30, 80), 4
        )
        == -54.0686
    )


def test_sun_angle_bounds():
    # Latitude out of bounds
    with pytest.raises(ValueError):
        pydaynight.sun_angle(datetime.datetime(2000, 1, 1), 95, 0)

    # Longitude out of bounds
    with pytest.raises(ValueError):
        pydaynight.sun_angle(datetime.datetime(2000, 1, 1), 0, 190)

    # Elevation out of bounds
    with pytest.raises(ValueError):
        pydaynight.sun_angle(datetime.datetime(2000, 1, 1), 0, 0, -10)


def test_sun_angle_array():
    # Array input no elevation
    assert (
        pydaynight.sun_angle(
            datetime.datetime(1900, 1, 1),
            np.array([90, 45, 0, -45, -90]),
            np.array([-180, -90, 0, 90, 180]),
        ).round(4)
        == np.array([-23.0514, -15.4905, -66.9333, 15.4905, 23.0514])
    ).all()

    # Array input with elevation
    assert (
        pydaynight.sun_angle(
            datetime.datetime(1900, 1, 1),
            np.array([90, 45, 0, -45, -90]),
            np.array([-180, -90, 0, 90, 180]),
            80,
        ).round(4)
        == np.array([-14.0180, -6.4570, -57.8999, 24.5239, 32.0849])
    ).all()
