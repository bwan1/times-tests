from times import *
import pytest

def test_given_input():
    """Standard results"""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    """Two time ranges that do not overlap"""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_intervals():
    """Two time ranges that both contain several intervals each"""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00", 2, 60) #10-15 16-31
    short = time_range("2010-01-12 10:15:00", "2010-01-12 10:46:00", 2, 60) #15-30 31-46
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:15:00', '2010-01-12 10:15:00'), ('2010-01-12 10:16:00', '2010-01-12 10:30:00'), ('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    assert result == expected

def test_end_to_end():
    """Two time ranges that end exactly at the same time when the other starts"""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:31:00")
    short = time_range("2010-01-12 10:31:00", "2010-01-12 10:46:00")
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:31:00', '2010-01-12 10:31:00')]
    assert result == expected

def test_time_range_backwards():
    with pytest.raises(ValueError, match=r"End time: .* is before start time: .*\."):
        time_range("2010-01-12 10:45:00", "2010-01-12 10:31:00")