import allure
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import create_booking_payload
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that the booking is created via payload with correct status code")
    @allure.description("Create a booking through positive payload and verify the response code as 200 ")
    def test_positive(self):
        response=post_request(url=APIConstants.create_booking_url(self), headers=Utils().common_headers_json(),
                              auth=None, payload=create_booking_payload(), in_json=False)
        booking_id=response.json()["bookingid"]
        verify_http_response_code(response=response,expected_data=200)
        verify_json_key_booking_id_not_null(booking_id)

    @pytest.mark.negative
    @allure.title("Verify the booking via empty payload with correct status code")
    @allure.description("Create a booking through empty payload and verify the response code as 500")
    def test_negative(self):
        response=post_request(url=APIConstants.create_booking_url(self), headers=Utils().common_headers_json(),
                                      auth=None, payload={}, in_json=False)
        verify_http_response_code(response=response,expected_data=500)
