import pytest


@pytest.mark.smoke
def test_method1():
    print("Inside test_method1.")
    assert 5 == 6


@pytest.mark.smoke
def test_method2():
    print("Inside test_method2.")
    assert 5 == 5
