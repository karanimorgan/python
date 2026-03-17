number = int(input("Enter a number:"))

while number >= 0 :
    print(f"You entered: {number}")
    number = int(input("Enter another number(or a negative number to stop):"))
print("You've entered a negative number. Goodbye!")