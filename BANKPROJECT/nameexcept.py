#WAPP which will validate the name
#DATA VALIDATIONS
# Name must be purely alphabets.
# if name contains any digits or special symbol then raise the exception InvalidNameError(Programmer defined).
# if the name is only space then raise SpaceError.
# if the length is zero then raise ZeroLengthError.
class InvalidNameError(Exception):pass
class SpaceError(BaseException):pass
class ZeroNameLengthError(Exception):pass