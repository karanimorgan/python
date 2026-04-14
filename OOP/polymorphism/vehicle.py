class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class car (Vehicle):
    def move(self):
        return "The car is driving on the road."
    
class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water."
    
class Plane(Vehicle):
    def move(self):
        return "The plane is flying in the sky."

def show_vehicle_movement(vehicle):
    print(vehicle.move())

vehicles = [car(), Boat(), Plane()]

for v in vehicles:
    show_vehicle_movement(v)