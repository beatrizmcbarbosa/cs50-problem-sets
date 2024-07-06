from fuel import convert, gauge
import pytest

# Convert tests
def test_convert():
    assert convert('1/2') == 50
    with pytest.raises(ValueError):
        assert convert('cat/dog')
    with pytest.raises(ValueError):
        assert convert('2/1')
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0')


# Gauge tests
def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(33) == '33%'

