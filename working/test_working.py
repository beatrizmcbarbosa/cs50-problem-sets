from working import convert
import pytest

def test_hours():
    assert convert("5 PM to 10 PM") == "17:00 to 22:00"
    assert convert("7 AM to 11 AM") == "07:00 to 11:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_minutes():
    assert convert("5 PM to 10:05 PM") == "17:00 to 22:05"
    assert convert("5:30 AM to 10 AM") == "05:30 to 10:00"
    with pytest.raises(ValueError):
        assert convert("5:70 AM to 6:70 AM")

def test_to():
    with pytest.raises(ValueError):
        assert convert("5 AM - 6 AM")
    with pytest.raises(ValueError):
        assert convert("5 AM  6 AM")

def test_invalidTimes():
    with pytest.raises(ValueError):
        assert convert("13 AM  14 PM")
