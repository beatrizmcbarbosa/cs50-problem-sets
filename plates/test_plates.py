from plates import is_valid

def test_alphabetical():
    assert is_valid('2222') == False
    assert is_valid('AA2222') == True

def test_length():
    assert is_valid('A22222') == False
    assert is_valid('AA22222') == False
    assert is_valid('AA2222') == True
    assert is_valid('AA') == True

def test_numbers():
    assert is_valid('AAA22A') == False
    assert is_valid('AA00') == False
    assert is_valid('AA1234') == True

def test_alphanumeric():
    assert is_valid('PI3.14') == False
    assert is_valid(' AA22 22') == False