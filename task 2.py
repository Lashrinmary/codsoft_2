def calculator():
    print("Welcome to the Simple Calculator")
    print("You can perform: Addition (+), Subtraction (-), Multiplication (*), Division (/)")
    
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Performing the operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid operation. Please choose +, -, *, or /")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator function
calculator()
