import pytest
from age import categorise_byage 

def test_child():
    assert categorise_byage(1) == "child"
    assert categorise_byage(5) == "child"
    assert categorise_byage(9) == "child"
def test_teenager():
    assert categorise_byage(10) == "teenager"
    assert categorise_byage(15) == "teenager"
    assert categorise_byage(18) == "teenager"
def test_adult():
    assert categorise_byage(19) == "adult"
    assert categorise_byage(30) == "adult"
    assert categorise_byage(64) == "adult"
def test_golden_age():
    assert categorise_byage(65) == "golden age"
    assert categorise_byage(70) == "golden age"
    assert categorise_byage(120) == "golden age"
def test_invalid_age():
    assert categorise_byage(-1) == "invalid age: -1"
    assert categorise_byage(130) == "invalid age: 130"