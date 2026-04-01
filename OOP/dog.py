class Dog:
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.breed} owned by {self.owner}"
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old")

bosco = Dog("Bosco", 3, "Labrador retriever", "Alice")
simba = Dog("Simba", 5 ,"German Shepherd", "Bob")
# print(f"{bosco.name} is a {bosco.age}-year-old {bosco.breed} owned by {bosco.owner}")
# print(f"{simba.name} is a {simba.age}-year-old {simba.breed} owned by {simba.owner}")
# print(bosco)
# print(simba)

# celebrate birthdays
bosco.birthday()
simba.birthday()

