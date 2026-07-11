import random

secret_number = random.randint(1, 100)
guess = -1
attempts = 0

while guess != secret_number:
    attempts += 1
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Try a lower number")
    elif guess < secret_number:
        print("Try a higher number")
    else:
        print("Correct number!")

print(f"You guessed the number correctly in {attempts} attempts")
print(f"The secret number was {secret_number}")
print("Thank you for playing!") 