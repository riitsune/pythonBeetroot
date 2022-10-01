'''
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
'''
#version1

def oops():
    raise IndexError ("list is out of range, I guess!")

def trying():
    list1 = range(0, 10)
    try:
        print(list1[12])
    except IndexError:
        raise oops()
print(trying())

#version2

def oops():
    raise KeyError ("oops, no key in the set of existing keys!")

def trying():
    my_dict = dict(key1=0,
                   key2=1,
                   key3=3)
    try:
        print(my_dict[5])
    except KeyError:
        raise oops()
print(trying())
