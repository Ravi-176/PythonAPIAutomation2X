from faker import Faker
import json
faker=Faker()
def create_booking_payload():
    payload={
    "firstname" : "Sumit",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
        },
    "additionalneeds" : "Breakfast"
    }
    return payload
def create_booking_payload_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100,max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast","Television","WiFi","Parking"))
    }
    return payload
def create_token_payload():
    payload={
        "username": "admin",
        "password": "password123"
    }
    return payload
def partial_update_payload():
    payload={
    "firstname" : "Aayush",
    "lastname" : "Brown"
    }
    return payload