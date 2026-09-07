print("*** BMI CALCULATOR ***")
print()
Weight = float(input("Enter your weight (in kg) : "))
Height = float(input("Enter your height (in meters) : "))
print()

print("*** RESULT ***")
print("Weight : ",Weight)
print("Height : ",Height,"m")
BMI = Weight / (Height * Height)
print(f"BMI : {BMI:.3f}")
if(BMI < 18.5):
    print("Category : Underweight")
elif(BMI >= 18.5 and BMI <= 24.9):
    print("Category : Normal Weight")
elif(BMI >= 25 and BMI <= 29.9):
    print("Category : Overweight")
else:
    print("Category : Obese")
print()
print("*** Thank You! ***")

