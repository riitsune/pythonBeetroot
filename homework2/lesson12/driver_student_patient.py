'''
. Create classes that will describe a Bus Driver, a Student and a Patient of the Hospital.
Add any attributes and methods essential for each one in your opinion.
 By desire you may use an inheritance principle to gather common attributes and methods into some parent class.

'''
class Person:
    def __init__(self, name, gender, age, nationality):
        self.name = name
        self.gender = gender
        self.age = age
        self.nationality = nationality


    def __repr__(self):
        return (self.name+ ","+ self.gender+","+str(self.age) +","
                +self.nationality +"," + self.occupation +"," + self.marital_status)


class BusDriver(Person):
    def __init__(self, name, gender, age, nationality, salary, route,experience, licence_category):
        super().__init__(name, gender, age, nationality)
        self.salary = salary
        self.route = route
        self.experience = experience
        self.licence_category = licence_category

    def greetings(self):
        return "Good morning, please show your ticket, young man!"


class Student(Person):
    def __init__(self,name, gender, age, nationality, uni, study_status, faculty, grades, group, activities):
        super().__init__(name, gender, age, nationality)
        self.uni = uni
        self.study_status = study_status
        self.faculty = faculty
        self.grades = grades
        self.group = group
        self.activities = activities

    def perfomance(self):
        return self.grades


class HospitalPatient(Person):
    def __init__(self, name, gender, age, nationality, history, doctor, sickness, insurance):
        super().__init__(name, gender, age, nationality)
        self.history = history
        self.doctor = doctor
        self.sickness = sickness
        self.insurance = insurance

    def status(self, sickness):
        if sickness == 0:
            print("Patient will be discharged from the hospital soon")


bus_driver = BusDriver("Alexandro Garcia", "male", "54", "Spanish", "100 euro", "Marytown School for disabled", "27 years", "has a licence, category B,C, D")
student = Student("Mimi Johansson", "female", "20", "Swedish", "Harvard", "3rd year bachelor degree", "Architecture", "A,B, B, C", "34-F", "volleyball, piano")
patient = HospitalPatient("Marsel Leon", "male", "96", "French", "inherited diabetes", "dr.Magnus", "bone fracture", "general medical insurance")


print(bus_driver.greetings())
print(student.perfomance())
print(patient.status(0))
