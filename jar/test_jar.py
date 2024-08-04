from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(1)
    assert jar.size == 11
    with pytest.raises(ValueError):
        assert jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(9)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        assert jar.withdraw(1)
