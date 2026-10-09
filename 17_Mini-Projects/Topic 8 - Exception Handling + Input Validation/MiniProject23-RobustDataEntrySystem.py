DetailBox = []
while(1):
    print("===== Robust Data Entry System =====\n")
     
    print("1. Add student")
    print("2. View student")
    print("3. Exit\n")

    choice = int(input("Enter your choice: "))
    print()

    if(choice == 1):
        name = input("Enter Name :")
        while(1):
            try:
                age = int(input("Enter age : "))
                if(age>=5 and age<=100):
                    break
                else: 
                    print("The allowed age range is 5–100.") 
                    print()
            except:
                print("Please enter a valid number for age.")
                print()

        while(1):
            try:
                marks = int(input("Enter marks : "))
                if(marks>=0 and marks<=100):
                    break
                else: 
                    print("The allowed marks range is 0–100.") 
                    print()

            except:
                print("Please enter a valid number for marks.")
                print()
           
        email = input("Enter email : ")

        information = {
            "Name" :   name,
            "Age" :    age,
            "Marks" :  marks,
            "Email" :  email
        }

        DetailBox.append(information)

    elif(choice == 2):
        for i in DetailBox:
            print("Name : ",i["Name"])
            print("Age : ",i["Age"])
            print("Marks : ",i["Marks"])
            print("Email : ",i["Email"])
            print()

    elif(choice == 3):
        print("Goodbye! Thank you for using the Robust Data Entry System.")
        print()
        break

    else:
        print("Invalid Choice.")
        print()