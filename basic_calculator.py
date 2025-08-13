def basic_calculator():
    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))  # Convert input to float
        num2 = float(input("Enter the second number: "))  # Convert input to float
        operation = input("Enter the operation (+, -, *, /): ").strip()  # Get operation and remove whitespace
        
        # Perform the operation based on user input
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the program
basic_calculator()