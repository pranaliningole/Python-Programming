print("*** PYTHON QUIZ ***")
print()
print("Test your Python basics!")
score = 0
print()
print("Question 1")
print("What is the correct way to take input in Python?")
print()
print("A. print()")
print("B. input()")
print("C. scan()")
print("D. get()")
ans = input("Enter your answer : ")
if(ans == "B"):
    print("Congratulations! Your answer is correct")
    score+=1
elif(ans == "A"):
    print("Wrong")
elif(ans == "C"):
    print("Wrong")
elif(ans == "D"):
    print("Wrong")
else:
    print("Invalid option")
print()

print("Question 2")
print("Which data type is used for decimal numbers?")
print()
print("A. int")
print("B. str")
print("C. float")
print("D. bool")
ans = input("Enter your answer : ")
if(ans == "C"):
    print("Congratulations! Your answer is correct")
    score+=1
elif(ans == "A"):
    print("Wrong")
elif(ans == "B"):
    print("Wrong")
elif(ans == "D"):
    print("Wrong")
else:
    print("Invalid option")
print()

print("Question 3")
print("What is the result of 10 + 5?")
print()
print("A. 15")
print("B. 10")
print("C. 5")
print("D. 20")
ans = input("Enter your answer : ")
if(ans == "A"):
    print("Congratulations! Your answer is correct")
    score+=1
elif(ans == "B"):
    print("Wrong")
elif(ans == "C"):
    print("Wrong")
elif(ans == "D"):
    print("Wrong")
else:
    print("Invalid option")
print()

print("Question 4")
print("Which keyword is used to check another condition?")
print()
print("A. for")
print("B. elif")
print("C. while")
print("D. def")
ans = input("Enter your answer : ")
if(ans == "B"):
    print("Congratulations! Your answer is correct")
    score+=1
elif(ans == "A"):
    print("Wrong")
elif(ans == "C"):
    print("Wrong")
elif(ans == "D"):
    print("Wrong")
else:
    print("Invalid option")
print()


print("Question 5")
print("Which symbol is used to compare two values for equality?")
print()
print("A. =")
print("B. !=")
print("C. ==")
print("D. >=")
ans = input("Enter your answer : ")
if(ans == "C"):
    print("Congratulations! Your answer is correct")
    score+=1
elif(ans == "B"):
    print("Wrong")
elif(ans == "A"):
    print("Wrong")
elif(ans == "D"):
    print("Wrong")
else:
    print("Invalid option")
print()

print("*** QUIZ RESULT ***")
print("Total Questions : 5")
print("Correct Answers : ",score)
print("Wrong Answers   : ",5-score)
print("Final Score     : ",score,"/5")

