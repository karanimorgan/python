def square_numbers():
    numbers = [2, 3, 4, 5]
    # create an empty list to store the square numbers
    # use a for loop to iterate through the numbers and append their squares to the list
    # return the list of squred numbers
    
#     for number in numbers:
#         square = number ** 2
#         print(f"The square of {number} is {square}")
        
# square_numbers()  
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number **2)
    return squared_numbers
print(square_numbers())


  
    




