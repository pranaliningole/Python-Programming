import random
print("*** NUMBER GUESSING GAME ***")
random_number = random.randint(1, 100)
Attempt = 0
while(True):
    guess_number = int(input("Guess the number between 1 and 100 : "))
    if(random_number == guess_number):
        print("Congratulations! You guessed the correct number.")
        print("Attempts : ", Attempt)
        break
    elif(random_number < guess_number):
        print("Too High! Try again.")
        Attempt += 1
    else:
        print("Too Low! Try again.")
        Attempt += 1
