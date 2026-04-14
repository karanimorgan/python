class Person:
    def __init__(self, name, id):
        self.name =name
        self.id = id
        
    def greet(self):
        return f"Hello, my name is {self.name} .My ID is {self.id}."
    
class Employee(Person):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    
    def employee_info(self):
        return f"{self.greet()} I earn {self.salary} per year."

class Athlete:
    def __init__(self, sport):
        self.sport = sport
    def athlete_info(self):
        return f"I am an athlete and I play {self.sport}."


class Student(Employee, Athlete):
    def __init__(self, name, id ,salary, sport):
        super().__init__(name, id, salary)
        Athlete.__init__(self, sport)

    def student_athlete_info(self):
         return f"{self.employee_info()} I am also a student-athlete who plays {self.sport}."

student_athlete = Student("John Doe", 12345, 50000, "Basketball")
print(student_athlete.student_athlete_info())