print("*** FACTORIAL CALCULATOR ***")
print()
number = int(input("Enter a number : "))
print()
print("*** RESULT ***")
print("Number  : ",number)
factorial = 1
for i in range(1, number+1):
    factorial *= i
print("Factorial : ",factorial)
print("Thank You!")
