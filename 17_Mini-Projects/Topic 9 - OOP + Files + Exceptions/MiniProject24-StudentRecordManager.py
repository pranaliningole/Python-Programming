student_records = []

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

while True:
    print("================================\n")
    print("     STUDENT RECORD MANAGER\n")
    print("================================\n")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Save Records")
    print("7. Exit\n")

    choice = int(input("Enter your choice: "))
    print("\n")

    if choice == 1:
        print("----- Add Student -----\n")
        name = input("Enter student name: ")
        while True:
            try:
                marks = int(input("Enter student marks: "))
                if 0<=marks<=100:
                    break
                else:
                    print("Marks must be between 0 and 100.\n")
            except ValueError:
                print("Oops! it is the value error.")
        print("\nStudent added successfully!")
        add_student = Student(name, marks)
        student_records.append(add_student)

    elif choice == 2:
        print("----- View Students -----\n")
        if not student_records:
            print("No student records found.\n")
        else:
            for i in student_records:
                print("Name : ",i.name)
                print("Marks : ",i.marks)
                print()

    elif choice == 3:
        found = False
        print("----- Search Student -----")
        search_name = input("Enter student name:  ")
        print()
        for i in student_records:
            if i.name == search_name:
                found = True
                print("Student found!\n")
                print("Name  : ",i.name)
                print("Marks : ",i.marks)
                print()
        if found == False:
            print("Student not found.")
            print()

    elif choice == 4:
        print("----- Update Marks -----\n")
        update_name = input("Enter student name:  ")
        print()
        found = False
        for i in student_records:
            if update_name == i.name:
                found = True
                print("Student found!\n")
                print("Current Marks : ",i.marks)
                print()
                while True:
                    try:
                        new_marks = int(input("Enter new marks: "))
                        print()
                        if 0<=new_marks<=100:
                            i.marks = new_marks
                            print("\nMarks updated successfully!\n")
                            break
                        print("Marks must be between 0 and 100.\n")
                    except:
                        print("ValueError!!\n")
        if found == False:
          print("Student not found.")
                        

    elif choice == 5:
        print("----- Delete Student -----\n")
        delete_student = input("Enter student name: ")
        print()
        found = False
        for i in student_records:
            if(i.name == delete_student):
                found = True
                student_records.remove(i)
                print("\nStudent deleted successfully!")
                break
        if found == False:
            print("Student not found.")

    elif choice == 6:
        print("----- Save Records -----")
        with open("StudentsFile.txt","w") as file:
            for i in student_records:
                file.write(f"{i.name}, {i.marks}\n")
        print("Student records saved successfully\n!")

    elif choice == 7:
        print("Goodbye! Thank you for using the Student Record Manager")
        break

    else:
        print("Invalid Choice.")




    