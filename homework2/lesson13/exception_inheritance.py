'''
Create your own exception classes inherited from built in Python ones. 
Inherit one of them directly from Exception class and second - from some more specific class like RecursionError or UnicodeDecodeError.
'''

class SpecialTypeException(Exception):
    pass


user_i = int(input("Please give me a number"))
if not user_i.isdigit:
    raise SpecialTypeException("Must be only numbers")
