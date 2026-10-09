Notes = []
while(1):
    print("1. Create a note")
    print("2. View all notes")
    print("3. Search for a note")
    print("4. Delete a note")
    print("5. Exit")
    print()

    choice = int(input("Enter your choice : "))
    print()

    if(choice == 1):
        note = input("Enter your note: ")
        Notes.append(note)
        with open("Output.txt", "a") as file:
            file.write(note+"\n")
        print()

    elif(choice == 2):
        with open("Output.txt", "r") as file:
            for i in file:
                print(i)
                print()

    elif(choice == 3):
        search = input("Enter what you want to search: ")
        with open("Output.txt","r") as file:
            found = False
            for i in file:
                if search == i.strip():
                    print("Search results: ", i.strip())
                    found = True
                print()
                
            if not found:
               print("Note not found.")
               print()

    elif(choice == 4):
        deleteNode = input("Enter the note you want to delete : ") 
        remaining = []

        with open("Output.txt", "r") as file:
            found = False
            for i in file:
                if deleteNode == i.strip():
                    found = True
                    continue
                else:
                    remaining.append(i.strip())

            with open("Output.txt", "w") as file:
                for i in remaining:
                    file.wite(i + "\n")
                    print()

            if found == False:
                print("Note not found.")
                print()

    elif(choice == 5):
        print("Goodbye! Your notes have been saved.")
        print()
        break

    else:
        print("Option is invalid.")
        print()
                
            

    

