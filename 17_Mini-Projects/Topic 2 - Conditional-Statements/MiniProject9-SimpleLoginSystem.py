print("*** SIMPLE LOGIN SYSTEM ***")
print()
while(True):
    username = input("Enter username : ")
    password = input("Enter password : ")
    has_digit = False
    has_alpha = False
    for character in password:
        if(character.isdigit()):
            has_digit = True
        elif(character.isalpha()):
            has_alpha = True
    if(username.isalpha() and has_digit and has_alpha):
        print("Login Successful!")
        break;
    else:
        print("Invalid username or password!")
        print()
