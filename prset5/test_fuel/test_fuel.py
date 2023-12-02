from fuel import convert, gauge
import pytest

def test_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/Dog")
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ValueError):
        convert("1#2")
def test_convert_return():
    assert (str(convert("1/4"))).isnumeric() == True
    assert convert("1/4") == 25
    assert convert("2/4") == 50

def test_gauge_return():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"