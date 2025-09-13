import random

secret = random.randint(1, 10)
print("I picked a number between 1 and 10. Try to guess it!")

guess = None
count = 0

while guess != secret:
    guess = int(input("Your guess: "))
    count += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {count} guesses.")