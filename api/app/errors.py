class APIError(Exception):
    status_code = 500
    message = 'Internal server error'

    def __init__(self, message=None, status_code=500):
        self.message = message or self.message
        self.status_code = status_code or self.status_code

    def to_dict(self):
        return dict(message=self.message, status_code=self.status_code)


class DBConnectionError(APIError):
    message = 'DB Connection failed'
