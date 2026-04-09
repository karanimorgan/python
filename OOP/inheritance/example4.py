class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"vehicle {self.make} {self.model}"

# create a class car that inherits from vehicle
# class car will have an additional attribute "year", color
# and a method 'display_car_info' that displays the cars information including the year and the colour
class Car(Vehicle):
    def __init__(self, make, model, year, colour):
        super().__init__(make, model)
        self.year = year
        self.colour = colour

    def display_car_info(self):
        return f"{super().display_info()},{self.year}, {self.colour}."

car = Car("suzuki", "swift", 2020, "red")
print(car.display_car_info())