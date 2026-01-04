from nameexcept import *
def validate(name):
    if len(name)==0:
        raise ZeroNameLengthError
    elif name.isspace():
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if not word.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvalidNameError
#here we raise other error's first so that in special character or digit exception it will work.