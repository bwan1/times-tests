from times import *
import yaml
import pytest

with open('fixture.yaml') as yaml_file:
    yaml = yaml.safe_load(yaml_file)
    fixture = []
    for i in yaml:
        # USING eval IS POTENTIALLY UNSAFE BUT i guess it works
        time_range_1 = eval(i['time_range_1'])
        time_range_2 = eval(i['time_range_2'])
        expected = [eval(j) for j in i['expected']]
        fixture.append((time_range_1, time_range_2, expected))

@pytest.mark.parametrize("time_range_1, time_range_2, expected", fixture)
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