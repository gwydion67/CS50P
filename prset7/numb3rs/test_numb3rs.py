from numb3rs import validate

def test_0():
    assert validate('0.0.0.0') == True
    assert validate('275.0.3.3') == False

def test_big():
    assert validate('275.222.222.222') == False
    assert validate('2.2.2.266') == False

def test_cor():
    assert validate('3.23.45.23') == True
    assert validate('0.255.2.4') == True