def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!

    return 0


def test_days_between_dates():
    # test same day
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 30) == 0)
    # test adjacent days
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 31) == 1)
    # test new year
    assert (days_between_dates(2017, 12, 30,
                               2018, 1, 1) == 2)
    # test full year difference
    assert (days_between_dates(2012, 6, 29,
                               2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


test_days_between_dates()
