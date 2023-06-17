from art import logo3
from replit import clear

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }
    print(logo3)
    num1 = float(input("Enter the first number: "))
    
    for operator in operations:
        print(operator)
    
    end = False
    while(not end):
        operator_choice = input("Pick an Operator from the list: ")
        num2 = float(input("Enter the next number: "))
        result = operations[operator_choice](num1, num2)
        print(f"{num1} {operator_choice} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or typr 'n' to exit: ") == 'y':
            num1 = result
        else:
            end = True
            clear()
            calculator()

calculator()