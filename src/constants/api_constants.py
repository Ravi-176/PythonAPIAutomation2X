class APIConstants(object):
    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"
    @staticmethod
    def create_booking_url(self):
        return "https://restful-booker.herokuapp.com/booking"
    @staticmethod
    def create_token_url():
        return "https://restful-booker.herokuapp.com/auth"
    @staticmethod
    def put_patch_delete_url(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)