"""
You have a list [1, 2, 3, 4, 5, 6, 7, 0]. Write a function "try_to_return_a_number", which will take an argument
"number" and raise an exception OddError if number is odd, and ZeroError if number is zero. Write a high level function,
which will take an argument "list_of_numbers", go through it in for in loop, put every item from list to
"try_to_return_a_number" function, and print a number or a message depends on exception on each loop step.
"""


class OddError(Exception):
    pass


class ZeroError(Exception):
    pass


my_list = [1, 2, 3, 4, 5, 6, 7, 0]


def try_to_return_a_number(number):
    if number % 2 == 1:
        raise OddError
    elif number == 0:
        raise ZeroError


def the_high_level_function_big_lols(a_list):
    for element in a_list:
        try:
            try_to_return_a_number(element)
        except OddError:
            print('It\'s an \"odd\" error lolll!!')
        except ZeroError:
            print('Zero exception - no lolz.')
        else:
            print(f'The number is: {element}')


the_high_level_function_big_lols(my_list)


