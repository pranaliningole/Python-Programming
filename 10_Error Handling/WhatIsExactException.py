try:
    num = int(input("Enter the value : "))
    print("You entered : ", num)
except Exception as e:
    print("Something went wrong : ", str(e))
