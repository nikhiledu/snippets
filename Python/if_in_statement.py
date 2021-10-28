#!/usr/bin/python


class CustomError(Exception):

    def __init__(self, message="CustomError", status_code=None):
        Exception.__init__(self)
        self.message = message
        # Check if working in request context
        if request:
            self.response = jsonify(self.to_dict())
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = {'message': self.message}
        return rv


class NotSupportedError(CustomError):
    status_code = 422


class BackendError(CustomError):
    status_code = 500
    code = 500


class NotFoundError(CustomError):
    status_code = 404

class AlreadyExistsError(CustomError):
    status_code = 409


error = BackendError

if error in [ NotFoundError, AlreadyExistsError ]:
  print("Error '{}' found in list".format(error))
else:
  print("Error '{}' not found in list".format(error))
