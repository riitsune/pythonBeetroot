'''
Task 2

Doggy age

Create a class Dog with class attribute age_factor equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method human_age which returns the dog’s age in human equivalent.
'''
class Dog():
    age_factor: int = 7

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def human_age(self,age_factor, age):
        return int(age)*age_factor


dog_1 = Dog("Antonio", "5")

print(dog_1.human_age(7,5))
