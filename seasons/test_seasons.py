from seasons import get_dob, days_to_minutes
import pytest

def test_exit():
    with pytest.raises(SystemExit):
        assert get_dob("January 1, 1990")
    with pytest.raises(SystemExit):
        assert get_dob("cat")


def test_minutes():
    assert get_dob("2024-08-02") == 2
    assert days_to_minutes("2024-08-02") == "Two thousand, eight hundred eighty minutes"
