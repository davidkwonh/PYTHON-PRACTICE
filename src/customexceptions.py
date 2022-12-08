class CustomException(Exception):
    pass


def causeError():
    raise CustomException('You called the causeError function!')


causeError()

#   Common uses for these types of exceptions is raising HTTP classes
class HttpException(Exception):
    statusCode = None
    message = None

    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')


class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'


class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'


def raiseServerError():
    raise ServerError()


raiseServerError()

# ServerError                               Traceback (most recent call last)
# Input In [4], in <module>
#      15 def raiseServerError():
#      16     raise ServerError()
# ---> 18 raiseServerError()
#
# Input In [4], in raiseServerError()
#      15 def raiseServerError():
# ---> 16     raise ServerError()
#
# ServerError: Status code: 500 and message is: The server messed up!