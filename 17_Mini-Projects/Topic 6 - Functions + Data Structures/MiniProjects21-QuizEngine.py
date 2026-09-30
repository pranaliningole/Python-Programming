print("*** QUIZ ENGINE ***")
print()

iscreated = False

while(1):
    print("1. Create Quiz")
    print("2. Take Quiz")
    print("3. Exit")

    choice = int(input("Enter your choice : "))
    print()

    if choice == 1:
        print("=== Create Quiz ===")
        print()

        title = input("Enter quiz title: ")
        print()

        noQue = int(input("How many questions? "))
        print()

        questions = []

        for i in range(1, noQue+1):
            question = input("Enter your question : ")
            print()
            options = []
            for j in range(1, 5):
                option = input(f"Enter {j} your options : ")
                options.append(option)
            print()
            answer = input("Enter your answer : ") 
            print()
            One_Question = {
                "question" : question,
                "options" : options,
                "answer" : answer
            }
            questions.append(One_Question)
        print()
        print("Quiz is created")
        iscreated = True
        print()


    elif(choice == 2):
        if iscreated == True:
            print("*** Take Quize ***")
            score  = 0

            for i in questions:
                print("Que : ",i["question"])
                for j in i["options"]:
                    print("Option : ",j)
                ans = input("Enter your answer : ")
                print()
                if(ans == i["answer"]):
                    score += 1
            print("Score = ", score)
            print()

        else:
            print("Quize is not created.")
            print("Create quize first")
            print()
            continue

    elif(choice == 3):
        print("Thank You")
        print("Quize is exiting")
        print()
        break
                
    
        
