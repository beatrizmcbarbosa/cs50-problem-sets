from um import count

def test_um():
    assert count("um") == 1
    assert count("umm") == 0

def test_spaces():
    assert count("um um") == 2

def test_case():
    assert count("Um") == 1
