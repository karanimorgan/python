class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def get_student_info(self):
        return f"{self.get_details()}, Student ID: {self.student_id}, Grade: {self.grade}"
    
class Teacher(Person):
    def __init__(self,name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def get_teacher_info(self):
        return f"{self.get_details()}, Employee ID: {self.employee_id}, Subject: {self.subject}"
    
student = Student("Alice", 15, 546, "A")
print(student.get_student_info())

teacher = Teacher("Mr. Smith", 40, 5678, "Math")
print(teacher.get_teacher_info())