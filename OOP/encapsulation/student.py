class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive.")

class Student(Person):
    def __init__(self, name, age, registration_number):
        super().__init__(name, age)
        self._registrarion_number = registration_number
    def display_info(self):
        return super().display_info()
        print(f"Registration number: {self._registration_number}")

student = Student("Alice", 20, "s6378")
student.display_info()
student.set_age(21)
student.display_info
print(student._age)
        