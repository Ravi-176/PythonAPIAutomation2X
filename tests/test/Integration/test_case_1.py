import allure
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils



class TestPostPatch(object):
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
    def test_partial_update(self,create_token,create_booking):
        token=create_token
        booking_id=create_booking
        patch_url=APIConstants.put_patch_delete_url(self,booking_id=booking_id)
        response=patch_request(url=patch_url,
                               headers=Utils().common_header_put_patch_delete_cookie(token=token),
                               auth=None,payload=partial_update_payload(),in_json=False)
        verify_http_response_code(response=response,expected_data=200)
        verify_response_key_not_none(response.json()["firstname"])
        verify_response_key(response.json()["firstname"],"Aayush")
