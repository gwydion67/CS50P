import pytest
from seasons import getMinutes, checkDob

def test_getMinutes():
    assert getMinutes('2002-09-13') == 'Eleven million, one hundred fifty-seven thousand, one hundred twenty minutes'

def test_checkDob():
    assert checkDob('2002-09-13') == '2002-09-13'
