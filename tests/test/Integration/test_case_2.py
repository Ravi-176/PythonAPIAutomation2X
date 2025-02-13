import allure
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils

# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

class TestPostDeleteVerify(object):
    @pytest.fixture()
    def create_token(self):
        response=post_request(url=APIConstants.create_token_url(self),headers=Utils().common_headers_json(),auth=None,payload=create_token_payload(),
                            in_json=False)
        verify_http_response_code(response=response,expected_data=200)
        verify_json_key_not_null_for_token(response.json()["token"])
        return response.json()["token"]
    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIConstants.create_booking_url(self), headers=Utils().common_headers_json(),
                                auth=None, payload=create_booking_payload(), in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_response_code(response=response, expected_data=200)
        verify_json_key_booking_id_not_null(booking_id)
        return booking_id
    def test_delete_booking(self,create_booking,create_token):
        booking_id=create_booking
        token=create_token
        delete_url=APIConstants.put_patch_delete_url(self,booking_id=booking_id)
        response=delete_request(url=delete_url,
                                headers=Utils().common_header_put_patch_delete_cookie(token=token),
                                auth=None,payload={},in_json=False)
        verify_http_response_code(response=response,expected_data=201)
        verify_response_delete(response=response.text)
    def test_get_booking(self,create_booking):
        booking_id=create_booking
        url=APIConstants.base_url(self)
        get_url=url+"/"+str(booking_id)
        response=get_request(url=get_url,auth=None)
        verify_http_response_code(response=response,expected_data=404)
        verify_response_404_get(response.text)