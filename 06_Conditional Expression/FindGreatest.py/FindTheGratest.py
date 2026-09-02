num = []
for i in range(4):
    element = int(input("Enter the value : "))
    num.append(element)
print("The gratest number is : ")
if(num[0] > num[1] and num[0] > num[2] and num[0] > num[3]):
    print(num[0])
elif(num[1] > num[0] and num[1] > num[2] and num[1] > num[3]):
    print(num[1])
elif(num[2] > num[1] and num[2] > num[0] and num[2] > num[3]):
    print(num[2])
else:
    print(num[3])