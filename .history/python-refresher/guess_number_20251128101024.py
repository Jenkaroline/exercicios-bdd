number = 8
answer = input("Do you want to guess the number? (yes/no): ")

guess = input("Guess the number: ")

if guess in number:
    print("You guessed it right!")
else:
    print("Try again!")