'''
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

    the call make_operation('+', 7, 7, 2) should return 16
    the call make_operation('-', 5, 5, -10, -20) should return 30
    the call make_operation('*', 7, 6) should return 42  

'''


def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == "-":
        sub_result = args[0]
        for arg in args:
            sub_result -= arg
        return sub_result
    elif operator == "*":
        multi = 1
        for arg in args:
            multi *= arg
        return multi

    try:
        str(make_operation)

    except TypeError:
        print("Please type only numbers!")

result = make_operation("*", 5,7,3)

print(result)
