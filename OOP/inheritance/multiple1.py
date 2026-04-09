class Person:
    def get_details(self):
        return "I am a person"

class Athlete:
    def get_skills(self):
        return "I am an athlete"
    
class Student(Person, Athlete):
    pass

student = Student()
print(student.get_details())
print(student.get_skills())
print(Student.__mro__)
    