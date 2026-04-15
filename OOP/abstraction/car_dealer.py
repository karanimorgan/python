class  Car:
    def __init__(self, name):
        self.name = name

class CarDealer:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        car = Car(car)
        self.cars.append(car)

    def show_cars(self):
        print("The dealer has the following cars:")
        for car in self.cars:
            print(f"- {car.name}")

dealer = CarDealer()
dealer.add_car("Toyota land cruiser")
dealer.add_car("Honda civic")
dealer.add_car("Dodge durango")
dealer.show_cars()