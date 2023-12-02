from twttr import shorten

def test_oneword():
    assert shorten("word") == "wrd"
    assert shorten("Abhishek") == "bhshk"

def test_line():
    assert shorten("My name is") == "My nm s"

def test_num():
    assert shorten("hello 1 person") == "hll 1 prsn"
def test_punc():
    assert shorten("hello,person") == "hll,prsn"