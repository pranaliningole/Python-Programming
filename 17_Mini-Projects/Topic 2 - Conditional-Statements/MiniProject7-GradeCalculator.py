print("*** GRADE CALCULATOR ***")
print()
maths = int(input("Enter marks for Mathematics : "))
physics = int(input("Enter marks for Physics : "))
english = int(input("Enter marks for English : "))
computer = int(input("Enter marks for Computer : "))
chemistry = int(input("Enter marks for Chemistry : "))
print()

print("*** RESULT ***")
print("Mathematics : ",maths)
print("Physics : ",physics)
print("Chemistry :",chemistry)
print("English : ",english)
print("Computer : ",computer)
print()

print("Total Marks : ",maths+physics+chemistry+english+computer)
Percentage = (maths+physics+chemistry+english+computer)/5
print("Percentage : ",Percentage)
if(Percentage >= 90):
    print("Grade : A+ ")
elif(Percentage >= 80):
    print("Grade : A")
elif(Percentage >= 70):
    print("Grade : B")
elif(Percentage >= 60):
    print("Grade : C")
elif("Percentage >= 50"):
    print("Grade : D")
else:
    print("Grade : Fail")
