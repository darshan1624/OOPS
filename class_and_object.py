class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender 
    
    def introduce(self):
        print(f'I am {self.name}, {self.age} years old')
    
    def sleep(self):
        print(f'sleeping for 8 hours')


class Student(Person):
    def __init__(self, name, age, gender, rollno, major):
        super().__init__(name,age,gender)
        self.rollno = rollno
        self.major = major
        
    def showprofile(self):
        print(f"rollno: {self.rollno}, major: {self.major}")
    
    def study(self):
        print('studying')

class EngineeringStudent(Student):
    def __init__(self,name,age,gender, rollno, major, specialization, codinglanguages):
        super().__init__(name,age,gender, rollno, major)
        self.specialization = specialization
        self.codinglangauges = self.codinglangauges
    
    def showprofile(self):
        print(f'rollno: {self.rollno},specialization: {self.specialization}')
        print(f'kows: {self.codinglangauges}')
    
    def buildproject(self):
        print(f'{self.name} is building an IOT based automtion project.')