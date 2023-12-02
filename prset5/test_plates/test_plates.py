from plates import is_valid


def test_smallerlength():
    assert is_valid("A") == False
    assert is_valid("2") == False
    assert is_valid("A2") == False

def test_largerlength():
    assert is_valid("AA222222") == False
    assert is_valid("AAA222") == True

def test_zero():
    assert is_valid("AAA022") == False
    assert is_valid("AAA202") == True

def test_punc():
    assert is_valid("AA@222") == False
    assert is_valid("ASDF") == True

def test_three():
    assert is_valid("AAA") == True

def test_inbetween():
    assert is_valid("AA2AA") == False

