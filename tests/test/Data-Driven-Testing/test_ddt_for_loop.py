import openpyxl
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.api_request_wrapper import *
def read_credentials(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(filename=file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({
            "username":username,
            "password":password
        })
    return credentials
def auth_request(username,password):
    payload={
        "username":username,
        "password":password
    }
    response=post_request(url=APIConstants().create_token_url(),
                          headers=Utils().common_headers_json(),
                          auth=None,payload=payload,in_json=False)
    return response
def test_create_auth_with_excel():
    file_path="C:/Users/somes/PycharmProjects/PythonAPIAutomation2X/tests/test/Data-Driven-Testing/test_ddt.xlsx"
    credentials=read_credentials(file_path=file_path)
    print(credentials)
    for credential in credentials:
        username=credential["username"]
        password=credential["password"]
        print(username,password)
        response=auth_request(username=username,password=password)
        print(response.status_code)