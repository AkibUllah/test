__all__ = [
    "ERROR_CODE"
]

class HTTPErrorCodes(object):
    def prepare_success_response(self):
        response = {
            'type': 'Success',
            'message': "Data Successfully Save",
            'data': self,
            'status': 200
        }
        return response

    def get_prepare_success_response(self):
        response = {
            'type': 'Success',
            'message': "Data Successfully Return",
            'data': self,
            'status': 200
        }
        return response


    def prepare_error_response(self):
        response = {
            'type': 'error',
            'message': self,
            'data': "",
            'status': 400
        }
        return response

    def get_prepare_error_response(self):
        response = {
            'type': 'error',
            'message': self,
            'data': "",
            'status': 404
        }
        return response


class ErrorCodes(object):

    def __init__(self):
        self.http_codes = HTTPErrorCodes


# created instance
ERROR_CODE = ErrorCodes()
