import random

number = random.randint(1, 100)

for guesses in range(1, 6):
    guess = int(input("Guess the number between 1 and 100: "))
    if(guess < number):
        print("Your guess is too low!")
        print("You have", 5 - guesses, "guesses left.")
    if(number%2 == 0):
        print("The number is divisible by two!")
        print("You still have", 5 - guesses, "guesses left.")
    if(number%3 == 0):
        print("The number is divisible by three!")
        print("You still have", 5 - guesses, "guesses left.")
    if(guess > number):
        print("Your guess is too high!")
        print("You still have", 5 - guesses, "guesses left.")
    if(guess==number):
        print("Congratulations! You guessed the number!")
        break
    if(guesses==5):
        print("You have run out of guesses! The number was", number)
        break