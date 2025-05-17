secret = 156

while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try again")
