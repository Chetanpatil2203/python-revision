
# Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.
num1 = int(input("Enter a num1"))
num2 = int(input("Enter a num2"))
operator = input("Enter a operator")

match operator :
    case "+":
        print(num1+num2)
    case "-" :
        print(num1-num2)  
    case "*" :
        print(num1*num2)  
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero.")

    case "%":
        if num2 != 0:
            print(num1 % num2)
        else:
            print("Cannot find remainder with zero.")