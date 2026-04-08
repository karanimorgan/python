class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Employee(Person):
    def __init__(self, name ,age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def salutation(self):
        return f"{super().introduce()},my employee ID is {self.employee_id} and a salary of Ksh{self.salary}."
    
employee = Employee("Karani", 24, "245", 50000)
print(employee.salutation())