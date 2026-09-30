def Addition(a, b):
    return a + b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b

def Power(a,b):
    return a**b

def Modulus(a,b):
    return a%b

while(1):
    print("*** ADVANCED CALCULATOR ***")
    print()

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    print()

    if(choice == 7):
        print("Thank you for using the Advanced Calculator!")
        print("Goodbye!")
        break

    firstNum = float(input("Enter first number: "))
    SecNum = float(input("Enter second number: "))

    if(choice == 1):
        result = Addition(firstNum , SecNum)

    elif(choice == 2):
        result = Subtraction(firstNum , SecNum)

    elif(choice == 3):
        result = Multiplication(firstNum , SecNum)

    elif(choice == 4):
        result = Division(firstNum , SecNum)

    elif(choice == 5):
        result = Power(firstNum , SecNum)

    elif(choice == 6):
        result = Modulus(firstNum , SecNum)

    else:
        print("Invalid Case")
        continue

    print("Result: ",result)

    
