
number1 = int(input("Enter first number (from 0-9 : )"))
number2 = int(input("Enter second number (from 0-9: )"))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+' :
    uns = number1 + number2
elif operation == '-' :
    uns = number1 - number2
elif operation == '*' :
    uns = number1 * number2
elif operation == '/' :
    if number2 != 0:
        uns = number1 / number2
    else:
        uns = "error : division by zero"
else:
    uns = "invalid operation"

print("The unswer of" ,number1,operation,number2,"is :", uns)