import numpy as np
print("*** STUDENT MARKS ANALYZER ***")
students_marks = []
n = int(input("Enter number of students : "))
print()
for i in range(1, n+1):
    marks = int(input(f"Enter marks for Student {i} : ")) ## Use an f-string to display the updated value of i from the for loop.
# Write the variable inside curly brackets {}.
# Example: f"Student {i}" → Student 1, Student 2, Student 3, ...
    students_marks.append(marks)
print()
marks_array = np.array(students_marks)
print("Student Marks: \n")
print(marks_array)
print()


print("*** Array Information ***")
print()
print("Number of Dimensions : ", marks_array.ndim)
print("Number of Elements : ",marks_array.size)
print("Shape : ",marks_array.shape)
print("Data Type : ",marks_array.dtype)
print()

print("*** Indexing ***")
print()
print("First Student Marks  : ",marks_array[0]) # indexing starts from 0 to n-1
print("Last Student Marks  : ",marks_array[n-1])
print("Third Student Marks  : ",marks_array[2])
print()

print("*** Slicing ***")
print()
print("First Three Students : ",marks_array[0:3])
print("Last Three Students  : ",marks_array[n-3 : n])
print()

print("*** Marks Analysis ***")
print()
total_marks = 0
for i in range(len(marks_array)):
    total_marks += marks_array[i]
print("Total Marks  : ",total_marks)
total_elements = len(marks_array)
print("Average Marks : ",total_marks/total_elements)
print("Highest Marks : ",np.max(marks_array))
print("Lowest Marks  : ",np.min(marks_array))
print()