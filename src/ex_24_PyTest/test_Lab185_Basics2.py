import pytest


@pytest.mark.smoke
def test_signUp():
    print("Inside test_signUp.")
    assert 1 - 1 == 2


@pytest.mark.smoke
def test_signIn():
    print("Inside test_signIn.")
    assert 1 + 1 == 2
