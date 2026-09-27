shopping_list = []

while(1):
    print("*** SHOPPING LIST ***")
    print()
    print("1. Add item")
    print("2. View items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")
    print()

    choice = int(input("Enter your choice: "))
    print()

    if(choice == 1):
        item = str(input("Enter item: "))
        shopping_list.append(item)
        print()

    elif(choice == 2):
        for iteam in shopping_list:
            print(iteam)
        print()

    elif(choice == 3):
        print("Current items: ")
        for item in shopping_list:
            print(item)
        print()
        change = input("Which item do you want to update? ")
        position = shopping_list.index(change)
        changeWith = input("Enter the new item: ")
        shopping_list[position] = changeWith
        print()
        print("Updated list")
        for item in shopping_list:
            print(item)
        print()

    elif(choice == 4):
        for item in shopping_list:
            print(item)
        print()
        deleteItem = input("Which item do you want to delete? ")
        shopping_list.remove(deleteItem)
        print()
        print("Updated list")
        for item in shopping_list:
            print(item)
        print()

    elif(choice == 5):
        print("Thank you for using the Shopping List!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        print()


