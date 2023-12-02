from jar import Jar
import pytest

def test_init():
    jar = Jar(30)
    assert jar.capacity == 30
    assert jar.size == 0

    jar.deposit(10)
    assert jar.size == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(30)

    jar.deposit(15)
    assert jar.size == 15
    assert len(str(jar)) == 15

    with pytest.raises(ValueError):
        jar.deposit(30)


def test_withdraw():
    jar = Jar(30)

    jar.deposit(15)
    assert jar.size == 15
    jar.withdraw(5)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.withdraw(20)
