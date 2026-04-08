class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        return f"Name: {self.name}, ID: {self.id}"
    
class Student(Person):
    def study(self):
        return f"{self.name} is studying."
    
student = Student("Alice", "12345")
print(student.display_info())
print(student.study())