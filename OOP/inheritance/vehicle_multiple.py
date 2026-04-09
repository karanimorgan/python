class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
        print(f"Engine of type '{self.engine_type}' created.")

class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count
        print(f"Vehicle with {self.wheel_count} wheels created.")

class Vehicle(Engine, Wheels):
    def __init__(self, engine_type, wheel_count, brand):
        super().__init__(engine_type)
        Wheels.__init__(self, wheel_count)
        self.brand = brand
        print (f"Vehicle brand '{self.brand}' created.")

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Engine Type: {self.engine_type}")
        print(f"wheel count: {self.wheel_count}")

car = Vehicle("V8", 4, "Ford")
car.display_info()