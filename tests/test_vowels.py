import pytest
from programs import vowels

def test_vowels_with_no_vowels():
    assert vowels.vowels('zxcfgy') == 0

def test_vowels_with_vowels():
    assert vowels.vowels('start') == 1
