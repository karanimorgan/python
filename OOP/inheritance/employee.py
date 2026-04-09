class Employee:
    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.salary = salary
    def employee_info(self):
        return f"Employee Name: {self.name}, Age: {self.age},Employee ID: {self.employee_id}, Salary:{self.salary}"

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def manager_info(self):
        return f"{super().employee_info()}, Department: {self.department}"
    
    def increase_salary(self, amount):
        self.salary += amount
        return f"New salary:{self.salary} ,Employee :{self.name}, department: {self.department}"
    
manager =  Manager("John", 25 , "045", 25000, "Forensics")
print(manager.manager_info())
print(manager.increase_salary(10000))