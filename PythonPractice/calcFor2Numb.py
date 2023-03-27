firstNumber = input("What is your first number?")
operation = input("What operation  would you like to perform on the first number?")
secondNumber = input("What is your second number?")

if operation == "+":
    x = int(firstNumber) + int(secondNumber)
    print (x)

elif operation == "*":
    x = int(firstNumber) * int(secondNumber)
    print (x)

elif operation == "/":
    x = int(firstNumber) // int(secondNumber)
    y = int(firstNumber) % int(secondNumber)
    print ((str(x) + ", Remainder: " + str(y)))

elif operation == "-":
    x = int(firstNumber) - int(secondNumber)
    print (x)
