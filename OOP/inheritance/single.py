class School:
    def __init__(self, name, year_founded):
        self.name = name
        self.year_founded = year_founded
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Course(School):
    def __init__(self, name, year_founded, course_code):
        super().__init__(name,year_founded)
        self.course_code = course_code

    def add_course(self, course_code):
        self.course_code = course_code

machine_learning = Course("Golden Tech",2000,"ML-001")
machine_learning.add_student({"name": "John Doe", "reg_no": "GTC/001", "gender":"Male"})
print(machine_learning.students)