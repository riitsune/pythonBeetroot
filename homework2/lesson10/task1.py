'''
Task 1

Write a Python program to detect the number of local variables declared in a function.
'''

def count_vars():
    var1 = 4
    var2 = "hey you"
    var3 = [1,2,3,4,5]
    var4 = 1
print(count_vars.__code__.co_nlocals)
