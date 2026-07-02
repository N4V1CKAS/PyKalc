number_A = float(input("Enter your first number: "))
number_B = float(input("Enter your second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = number_A + number_B
elif operator == "-":
    result = number_A - number_B
elif operator == "*":
    result = number_A * number_B
elif operator == "/":
    if number_B == 0:
        print("Error: Can't divide by 0")
        exit()
    else:
        result = number_A / number_B
else:
    print("Error: That's not a valid operator")
    exit()

print(result)
