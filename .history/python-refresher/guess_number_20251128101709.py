answer = input("Do you want to play? (yes/no): ")

# if answer == "yes" or answer == "Yes" is equivalent to
if answer in ("yes",  "Yes"):
    number = int(input("Guess a number between 1 and 10: "))
    if number == 8:
        print("You guessed it right!")
    else:
        print("Wrong guess, try again!")
else:
    print("Maybe next time!")