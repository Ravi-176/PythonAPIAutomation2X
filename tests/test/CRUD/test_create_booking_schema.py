import allure
import pytest
import json
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verifications import *
from src.helpers.payload_manager import create_booking_payload
from src.utils.utils import Utils
class TestCreateBookingSchema(object):
    def load_schema(self,file_name):
        with open(file_name,'r') as file:
            return json.load(file)
    def test_create_booking_schema(self):
        response=post_request(url=APIConstants.create_booking_url(self),
                              headers=Utils().common_headers_json(),auth=None,
                              payload=create_booking_payload(),in_json=False)
        booking_id=response.json()["bookingid"]
        verify_http_response_code(response=response,expected_data=200)
        verify_json_key_booking_id_not_null(booking_id)
        file_path=os.getcwd()+"/schema.json"
        schema=self.load_schema(file_name=file_path)
        try:
            validate(instance=response.json(),schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("JSON Schema error")