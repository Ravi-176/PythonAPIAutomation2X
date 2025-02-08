
def verify_http_response_code(response,expected_data):
    assert response.status_code==expected_data,"Failed-ER!=AR"

def verify_json_key_booking_id_not_null(key):
    assert key!=0,"Failed Message-Key is non-empty "+str(key)
    assert key>0,"Failed Message-Key is greater than 0"
def verify_response_key_not_null(key):
    assert key is not None