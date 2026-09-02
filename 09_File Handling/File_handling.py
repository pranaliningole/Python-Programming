# Open the file in read mode
file = open("Notes.txt", "r")
# read the content
content = file.read()
print(content)
file.close()


#Auto close
with open("Notes.txt", "r") as file:
    content = file.read()
    print(content)

# creating new file new content
with open("output.txt", "w") as file:
    file.write("This is the Python program")

# crating new line content
with open("output.txt", "a") as file:
    file.write("\nCongratulations we have mastered Python.")