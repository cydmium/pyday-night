import datetime


def julian_day(time_of_interest: datetime.datetime) -> float:
    """ Compute the Julian day, i.e. number of days since Jan 1, 4713 BC 12 UT

    Parameters
    ----------
    time_of_interest: datetime.datetime
        What time you would like to compute the Julian Day of

    Returns
    -------
    float:
        Julian Day for time of interest
    """
    starting_point = 1721425.5  # Hard code julian_day(January 1, 1)
    start = datetime.datetime(1, 1, 1)
    diff = (
        time_of_interest - start
    ).total_seconds() / 86400  # Get days since January 1, 1
    return diff + starting_point
