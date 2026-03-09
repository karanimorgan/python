car = "Mazda"

if car == "Toyota":
    # print("This is a Toyota car.")
    pass
elif car == "Honda":
    # print("This is a honda car.")
    pass
else:
    # print("This car is not a Toyota or Honda car.")
    pass

def check_car(car):
    if car == "Toyota":
        print("This is a Toyota car.")
    elif car == "Honda":
        print("This is a Honda car.")    
    else:
        print(f"This is not a Toyota car. It is a {car}.")    
check_car("Toyota")
check_car("Honda")
check_car("Ford")