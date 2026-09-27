import numpy as np
print("*** MATRIX CALCULATOR ***")
print()

row = int(input("Enter number of rows : "))
columns = int(input("Enter number of columns : "))
print() 

matrixA = []
print("*** MATRIX A ***")
for i in range(1, row+1):
    for j in range(1, columns+1):
        value = int(input(f"Enter element [{i}][{j}]"))
        matrixA.append(value)
matrixA = np.array(matrixA)        
print(matrixA)
print()

matrixB = []
print("*** MATRIX B ***")
for i in range(1, row+1):
    for j in range(1, columns+1):
        value = int(input(f"Enter element [{i}{j}]"))
        matrixB.append(value)
matrixB = np.array(matrixB)  
print(matrixB)
print()

print("*** MATRIX OPERATIONS ***")
print()

print("Addition: ")
print
Addition = matrixA + matrixB
Addition = np.array(Addition)
print(Addition)
print()
 
print("Subtraction: ")
print
Subtraction = matrixA - matrixB
Subtraction = np.array(Subtraction)
print(Subtraction)
print()

print("Multiplication: ")
print
Multiplication = matrixA * matrixB
Multiplication = np.array(Multiplication)
print(Multiplication)
print()

print("Division: ")
print
Division = matrixA / matrixB
Division = np.array(Division)
print(Division)
print()

### print("*** Reshape ***")
print()
print("Reshape MatrixA = ",matrixA.reshape(columns, row))
print("Reshape MatrixB = ",matrixB.reshape(columns, row)) 