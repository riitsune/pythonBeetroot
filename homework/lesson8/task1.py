'''
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
'''

def oops():
    raise IndexError ("list is out of range, I guess!")

def trying():
    list1 = range(0, 10)
    try:
        print(list1[12])
    except IndexError:
        raise oops()
print(trying())
