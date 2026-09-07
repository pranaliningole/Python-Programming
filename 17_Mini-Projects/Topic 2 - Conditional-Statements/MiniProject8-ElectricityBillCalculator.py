print("*** ELECTRICITY BILL CALCULATOR ***")
print()
unit = int(input("Enter electricity units consumed : "))
print()
print("*** RESULT ***")
print()
print("Units Consumed : ",unit)
if(unit>=0 and unit <= 100):
    print("Bill Amount : ",unit*5)
elif(unit>100 and unit<=200):
    print("Bill Amount : ",unit*7)
elif(unit>200 and unit<=300):
    print("Bill Amount : ",unit*10)
else:
    print("Bill Amount : ",unit*12)