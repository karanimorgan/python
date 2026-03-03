# get()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict.get("name"))
# print(my_dict.get("city"))
# print(my_dict.get("country", "Not found")) 

another = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address":{
        "street": "123 Main Street",
        "city": "anytown",
        "zip": "12345",
        "co-ordinates":{
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    }
}
# print(another.get("courses")[1] ) 
# print(another.get("address")["co-ordinates"]["latitude"])
# print(another.get("address").get("co-ordinates").get("latitude"))
# items()
# print(my_dict.items())
# print(list(my_dict.items())[2] [1])

# keys()
# print(my_dict.keys())
# print(list(my_dict.keys())[0]) 

# values
# print(my_dict.values())
# print(list(my_dict.values())[2])


# pop()
# print(my_dict.pop("age"))
# print(my_dict.pop("country", "Not Found"))

# popitem()
popped = my_dict.popitem()
# print(popped)
# print(my_dict)

# update()
additional_info = {"country": "USA", "occupation": "Engineer"}
my_dict.update(additional_info)
# print(my_dict)