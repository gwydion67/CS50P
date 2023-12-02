from bank import value

def test_hello():
    assert value("hello abhi") == 0
    assert value("hello someone") == 0
    assert value("Hello somedude") == 0

def test_h():
    assert value("help me") == 20
    assert value("Hell yeah") == 20

def test_other():
    assert value("good morning") == 100
    assert value("Good AFternoon") == 100