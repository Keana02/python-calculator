def calculator():
    print("Please input a number:")
    x = float(input())
    
    print("Please enter another number:")
    y = float(input())
    
    print("Select operation:")
    print("1. Addition (x + y)")
    print("2. Subtraction (x - y)")
    print("3. Multiplication (x * y)")
    print("4. Division (x / y)")
    
    operation = input("Enter the number of your choice (1-4): ")
    
    if operation == '1':
        result = x + y
    elif operation == '2':
        result = x - y
    elif operation == '3':
        result = x * y
    elif operation == '4':
        if y != 0:
            result = x / y
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation selected!"
    
    return f"Result: {result}"

# Run the calculator
print(calculator())
