from times import *
import pytest

test_cases = [
    ( # Standard given input
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
         ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    ),
    ( # Two time ranges that do not overlap
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00"),
        []
    ),
    ( # Two time ranges that both contain several intervals each
        time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00", 2, 60), #10-15 16-31
        time_range("2010-01-12 10:15:00", "2010-01-12 10:46:00", 2, 60), #15-30 31-46
        [('2010-01-12 10:15:00', '2010-01-12 10:15:00'),
         ('2010-01-12 10:16:00', '2010-01-12 10:30:00'),
         ('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    ),
    ( # Two time ranges that end exactly at the same time when the other starts
        time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00"),
        time_range("2010-01-12 10:31:00", "2010-01-12 10:46:00"),
        [('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    )]

@pytest.mark.parametrize("time_range_1, time_range_2, expected", test_cases)
def test_compute_overlap_time(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected

def test_time_range_backwards():
    with pytest.raises(ValueError, match=r"End time: .* is before start time: .*\."):
        time_range("2010-01-12 10:45:00", "2010-01-12 10:31:00")

"""
For test coverage, run in terminal:
pytest --cov="." --cov-report html
python -m http.server -d htmlcov
"""