marks = []
failed = False
for i in range(3):
    num = int(input("Enter the marks : "))
    marks.append(num)
    if(marks[i] < 33):
        print("Fail")
        break
if not failed:
    percent = ((sum(marks))/300 ) *100
    if(percent >= 40):
        print("PASS")
    else:
        print("FAIL")