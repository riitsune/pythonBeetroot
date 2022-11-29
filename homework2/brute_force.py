'''
 Use existing password generator function to generate passwords from 4 to 8 characters long that will contain only digits.
 Create a function that will try to guess generated password by brute force, e.g. continuously trying out all possible combinations of characters in the password.
 That mean that for only-digits password  of 4 characters length you potentially should try combinations from '0000', '0001', '0002' ... to ... '9999'.
 If guessed variant is equal to generated password - your brute force function will return its value. Then create (or find existing) time measurement decorator,
 decorate your brute force function with it and perform measurements of execution time for passwords of different length. Add results of measurements to your source file as a comment.
'''
from itertools import chain, product
from time import perf_counter
from random import choices, randrange
from string import digits


def timer(fn):

    def inner(*args, **kwargs):
        start = perf_counter()
        fn(*args, **kwargs)
        end = perf_counter()
        return end - start

    return inner


def password_generator():
    length = randrange(4,9)
    password = ''.join(choices(digits, k=length))
    print(f'Your password is: {password}\n')
    return password


def brute_force(digits, max_length):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(digits, repeat=i)
            for i in range(1, max_length + 1)))
   

password_generator()
brute_force(digits, 8)






brute_force(digits, 8)
#
# your_digits = '1234567890'
# complete_list = []
# for current in xrange(10):
#     a = [i for i in your_digits]
#     for y in xrange(current):
#         a = [x+i for i in your_digits for x in a]
#     complete_list = complete_list+a


