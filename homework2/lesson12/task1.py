'''
Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. 
Make another method called talk() which makes prints a greeting from the person containing, for example like this:

"Hello, my name is Carl Johnson and I’m 26 years old"
'''


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talks(self):
        return (f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old.")

person_1 = Person("John", "Doe", "33")

print(person_1.talks())
