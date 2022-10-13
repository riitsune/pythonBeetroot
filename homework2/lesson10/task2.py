'''

Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
'''


def multiplier_by_3(x):
    return x*3

#fucntion returning double result of the function


def double(f):
    def result_func(x):
        return f(f(x))
    return result_func


result = double(multiplier_by_3)

print(result(2))
