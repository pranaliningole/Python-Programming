print("*** STUDENT GRADE MANAGEMENT SYSTEM ***")
print()

n = int(input("Enter number of students : "))
print()

student = []
for i in range(1 , n+1):
    print(f"Enter number of students : {i}")
    students_detail = {
        "name" : input("Enter student name : "),
        "marks" : int(input("Enter marks : "))
    }
    student.append(students_detail)
    print()

print("*** STUDENT RESULTS ***")
print()
for students_detail in student:
    print("Student Name : ",students_detail["name"])
    Students_marks = students_detail["marks"]
    print("Student marks : ", students_detail["marks"])
    if(Students_marks > 90):
        print("Grade : A+ ")

    elif(Students_marks > 85):
        print("Grade : A ")

    elif(Students_marks > 80):
        print("Grade : B+ ")
    
    elif(Students_marks > 75):
        print("Grade : B ")
    
    elif(Students_marks > 60):
        print("Grade : c ")
    
    else:
        print("Grade : Fail")
    

