print("*** SIMPLE INTEREST CALCULATOR ***")
print()
Principal_Amount = float(input("Enter Principal Amount : "))
Rate_of_Interest = float(input("Enter Rate of Interest : "))
Time = float(input("Enter Time (in years)  : "))
print()

Simple_Interest = (Principal_Amount * Rate_of_Interest *Time)/100
Total_Amount =  Principal_Amount + Simple_Interest

print("*** RESULT ***")
print("Principal Amount : ₹",Principal_Amount)
print("Rate of Interest : ",Rate_of_Interest,"%")
print("Time : ",Time," years")
print("Simple Interest : ₹",Simple_Interest)
print("Total Amount : ₹",Total_Amount)
print()
print(" Thank You! ")