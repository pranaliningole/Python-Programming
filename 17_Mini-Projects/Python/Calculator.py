class Calculator:

    def calculate(self, choice):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
            print("Addition : ", result)
            self.history.append(f"{num1} + {num2} = {result}")

        elif choice == 2:
            result = num1 - num2
            print("Subtraction : ",result)
            self.history.append(f"{num1} - {num2} = {result}")

        elif choice == 3:
            result = num1 * num2
            print("Multiplication : ",result)
            self.history.append(f"{num1} * {num2} = {result}")

        elif choice == 4:
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Division : ",result)
                self.history.append(f"{num1} / {num2} = {result}")

    def __init__(self):
        self.history = []

    def save_history(self):
        with open("HISTORY.txt", "w") as file:
            for item in self.history:
                file.write(item +"\n")

    def show_history(self):
        for item in self.history:
            print(item)


    def exit(self):
        print("================================\n")
        print("       GOODBYE!\n")
        print("================================\n")
        print("History saved successfully.\n")
        print("Thank you for using Simple Calculator.\n")



def main():
    cal = Calculator()

    print("================================\n")
    print("       SIMPLE CALCULATOR\n")
    print("================================\n")

    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Exit\n")

    print('Enter your choice from "1", "2", "3" ,"4" , "5" , "6"')
    choice =  int(input("Your choice : "))

    if choice in [1, 2, 3, 4]:
        cal.calculate(choice)

    elif choice == 5:
        cal.show_history()

    elif choice == 6:
        cal.exit()
