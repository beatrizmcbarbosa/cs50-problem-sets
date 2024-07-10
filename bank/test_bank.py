from bank import value

def test_lowercase():
    assert value('hello') == 0

def test_uppercase():
    assert value('HELLO') == 0

def test_h():
    assert value('halloween') == 20

def test_number():
    assert value('He110') == 20

def test_incorrect():
    assert value('dfksn') == 100