def calculator():
    a = float(input("enter the first number:"))
    b = float(input("enter the second number:"))
    operation = input("enter the operation (+, -, *, /):")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b 
    elif operation =="*":
        result = a * b
    elif operation =="/":
        if b != 0:
            result = a/b
        else:
            print("error: Division by zero is not allowed.")
            return
    else:
        (print("Invalid operation."))  
        return  
    
    print(f"The result of {a} {operation} {b} is {result}")
if __name__ == "__main__":
    calculator()