num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose an operation (add, subtract, multiply): ')
def add():
    total = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(total))
def subtract():
    total = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(total))
def multiply():
    total = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(total))
if operation == "add":
    add()
elif operation == "subtract":
    subtract()
elif operation == "multiply":
    multiply()
else:
    print("Invalid operation")