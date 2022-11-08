from times import *
import pytest


@pytest.mark.parametrize("large, short, expected", [
    #Standard Input
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), 
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        ), 

    #Two time ranges that do not overlap
    (
       time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
       time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00"),
       []
    ), 
    
    #Two time ranges that both contain several intervals each
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00", 2, 60),
        time_range("2010-01-12 10:15:00", "2010-01-12 10:46:00", 2, 60),
        [('2010-01-12 10:15:00', '2010-01-12 10:15:00'), ('2010-01-12 10:16:00', '2010-01-12 10:30:00'), ('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    ),
    
    #Two time ranges that end exactly at the same time when the other starts
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00"),
        time_range("2010-01-12 10:31:00", "2010-01-12 10:46:00"),
        [('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    )
    ])
def test_given_input(large, short, expected):
    result = compute_overlap_time(large, short)
    assert result == expected

# def test_given_input():
#     """Standard input"""
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_no_overlap():
#     """Two time ranges that do not overlap"""
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
#     result = compute_overlap_time(large, short)
#     expected = []
#     assert result == expected

# def test_several_intervals():
#     """Two time ranges that both contain several intervals each"""
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00", 2, 60) #10-15 16-31
#     short = time_range("2010-01-12 10:15:00", "2010-01-12 10:46:00", 2, 60) #15-30 31-46
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:15:00', '2010-01-12 10:15:00'), ('2010-01-12 10:16:00', '2010-01-12 10:30:00'), ('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
#     assert result == expected

# def test_end_to_end():
#     """Two time ranges that end exactly at the same time when the other starts"""
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00")
#     short = time_range("2010-01-12 10:31:00", "2010-01-12 10:46:00")
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
#     assert result == expected

def test_time_range_backwards():
    with pytest.raises(ValueError, match=r"End time: .* is before start time: .*\."):
        time_range("2010-01-12 10:45:00", "2010-01-12 10:31:00")

"""
For test coverage, run in terminal:
pytest --cov="." --cov-report html
python -m http.server -d htmlcov
"""