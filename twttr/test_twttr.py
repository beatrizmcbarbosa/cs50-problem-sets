from twttr import shorten

# Test for no vowels
def test_novowels():
    assert shorten('qwr') == 'qwr'

# Test for uppercase
def test_uppercase():
    assert shorten('WORd') == 'WRd'

# Test for lowercase
def test_lowercase():
    assert shorten('word') == 'wrd'

#Test for omitting punctuation
def test_punctuation():
    assert shorten('..word..') == '..wrd..'

# Test for omitting numbers
def test_number():
    assert shorten('word123') == 'wrd123'