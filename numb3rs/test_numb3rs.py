from numb3rs import validate

def test_range():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.123.123.123") == False
    assert validate("255.256.256.256") == False


def test_bytes():
    assert validate("256.123.123.123.123") == False
    assert validate("256.123.123") == False

def test_text():
    assert validate("cat") == False

