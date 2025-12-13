import pytest
import allure

@allure.title("To verify that the create booking is working.")
@allure.description("We are verifying the create booking feature.")
@pytest.mark.positive
@pytest.mark.regression
def test_create_booking_positive():
    print("Inside test_create_booking_positive.")
    assert 1 - 1 == 2


@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("Inside test_create_booking_negative_1.")
    assert 1 + 1 == 2

@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase check for the negative  create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("Inside test_create_booking_negative_2.")
    assert 1 + 1 == 2