contact = {}

while(1):
    print("*** CONTACT BOOK ***")
    print()
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    print()

    choice = int(input("Enter your choice : "))

    if(choice == 1):
        name = str(input("Enter name: "))
        phone = int(input("Enter phone number: "))
        email = str(input("Enter email: "))

        contact[name] ={
            "phone" : phone,
            "email" : email
        }

    elif(choice == 2):
        for name, detail in contact.items():
            print(name)
            print(detail)
        print()

    elif(choice == 3):
        search = input("Enter name to search: ")
        print()

        if search in contact:
            print("Contact found!")
            print("Name : ",search)
            print("Email : ",contact[search]["email"])
            print("Phone : ",contact[search]["phone"])
            print()
        else:
            print("Contact not found.")

    elif(choice == 4):
        ToUpdate = input("Enter name of contact to update: ")
        print()
        if ToUpdate in contact:
            print("Current details:")
            print("Phone: ",contact[ToUpdate]["phone"])
            print("Email: ",contact[ToUpdate]["email"])
            print()
            Updatedemail = input("Enter new email: ")
            UpdatedNumber = input("Enter new number: ")
            contact[ToUpdate] = {
                "email" : Updatedemail,
                "phone" : UpdatedNumber
            }
        else:
            print("Contact not found")

    elif(choice == 5):
      DeleteContact = input("Enter the contact to delete: ")
      print()
      if DeleteContact in contact:
        del contact[DeleteContact]
        print("Contact deleted!")
      else:
        print("Contact not found.")

    elif(choice == 6):
        print("Thank you for using the Contact Book!")
        print("Goodbye!")
        break

    else:
        print("Invalid option")



    
    
