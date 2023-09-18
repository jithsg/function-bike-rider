# Write a test for hello.py

from hello import marco


def test_marco():
    assert marco("Marco") == "Polo"
    assert marco("Marco") != "No!"
    assert marco("marco") == "No!"
