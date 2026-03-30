class Dog:
    def __init__(self):
        pass
# create an instance of the Dog class
my_dog = Dog()
simba = Dog()
bosco = Dog()
# print(my_dog)
# print(simba)
if my_dog == simba:
    print("my_dog and simba are the same instance.")
else:
    print("my_dog and simba are different instances.")