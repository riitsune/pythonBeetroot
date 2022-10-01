'''
Task 2

Write a function that takes in two numbers from the user via input(),
call the numbers a and b, and then returns the value of squared a divided by b,
construct a try-except block which raises an exception
if the two values given by the input function were not numbers,
 and if value b was zero (cannot divide by zero).
'''

a = int(input("Type here one number\n"))
b = int(input("Type here second number\n"))
def exception(a,b):

    return int(a ** 2) / int(b)

try:
    exception(a,b)
except ZeroDivisionError:
    print("Second number cannot be 0!")

try:
    exception(a,b)
except ValueError:
    print("Please, type numbers instead!")

print(exception(a,b))
