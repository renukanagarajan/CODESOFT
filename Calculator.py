print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")

option = int(input("Choose an operator: "))
result = 0

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    if result is not None:
        print("Result:", result)
else:
    print("Invalid operation entered")
