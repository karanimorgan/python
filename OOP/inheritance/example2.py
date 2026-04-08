class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        return f"Name: {self.name}, ID: {self.id}"
    
class Student(Person):
    def __init__(self, name, id, grade):
        # person.__init__(self, name, id)
        super().__init__(name, id)
        self.grade = grade
        
    def information(self):
        return f"{super().display_info()},Grade: {self.grade}"
    
student = Student("John Doe", "12345", "A")
print(student.information())