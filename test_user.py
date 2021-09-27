from user import whoopUser
import datetime


def test_datetime_with_tz():
    inp = "2020-05-11T06:03:59.22+00:00"
    tz = "+0100"
    got_dt = whoopUser.convert_whoop_str_to_datetime(inp, tz)
    expected_dt = datetime.datetime(
        2020,
        5,
        11,
        6,
        3,
        59,
        220000,
        tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
    )
    assert got_dt == expected_dt


def test_whoop_datetime():
    malformed_inputs = [
        "2020-05-11T06:03:59.22+00:00",
        "2021-09-08T21:41:06.83+00:00",
        "2020-06-30T22:02:51.87+00:00",
        "2020-07-05T22:44:02.1+00:00",
    ]
    expected_dts = [
        datetime.datetime(2020, 5, 11, 6, 3, 59, 220000, tzinfo=datetime.timezone.utc),
        datetime.datetime(2021, 9, 8, 21, 41, 6, 830000, tzinfo=datetime.timezone.utc),
        datetime.datetime(2020, 6, 30, 22, 2, 51, 870000, tzinfo=datetime.timezone.utc),
        datetime.datetime(2020, 7, 5, 22, 44, 2, 100000, tzinfo=datetime.timezone.utc),
    ]
    for idx, expected in enumerate(expected_dts):
        got_dt = whoopUser.convert_whoop_str_to_datetime(malformed_inputs[idx], "+0000")
        assert expected == got_dt
