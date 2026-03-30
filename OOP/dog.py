class Dog:
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

bosco = Dog("Bosco", 3, "Labrador retriever", "Alice")
simba = Dog("Simba", 5 ,"German Shepherd", "Bob")
print(f"{bosco.name} is a {bosco.age}-year-old {bosco.breed} owned by {bosco.owner}")
print(f"{simba.name} is a {simba.age}-year-old {simba.breed} owned by {simba.owner}")

