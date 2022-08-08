import random

print("--------------------WELCOME TO THE NUMBER GUESSING GAME!--------------------")
print("\n")
print("Instructions: -")
print("1. The computer will generate a random number between 1 and 100.")
print("2. You will have to guess the number.")
print("3. You will have to guess the number within 10 tries.")
print("4. If you guess the number correctly, your score will increase by 1.")
print("The maximum game score is 10.")
print("The minimum game score is 0.")
print("\n")

print("---------------------LET'S START THE GAME!---------------------")
number = random.randint(1, 100)
gamescore = 10
print('\n')

for guesses in range(1, 11):
    guess = int(input("Guess the number between 1 and 100: "))
    if(guess < number):
        print("Your guess is too low!")
        print("You have", 10 - guesses, "guesses left.")
        print('\n')
        gamescore -= 1
    if(guess > number):
        print("Your guess is too high!")
        print("You still have", 10 - guesses, "guesses left.")
        print('\n')
        gamescore -= 1
    if(guesses==1):
        if(number%2==0):
            print("HINT: The number is divisible by 2.")
            print('\n')
        if(number%3==0):
            print("HINT: The number is divisible by 3.")
            print('\n')
        if(number%7==0):
            print("HINT: The number is divisible by 7.")
            print('\n')
        if(number%10==0):
            print("HINT: The number is divisible by 10.")
            print('\n')
    if(guess==number and guesses==1):
        print("Congratulations! You won! You guessed the number in first attemp!")
        break
    if(guess==number):
        print("Congratulations! You won! You guessed the correct number!")
        break
    if(guesses==10):
        print("You have run out of guesses! The number was", number)
        break

print('\n')
print("Your final score is: ", gamescore)
print("\n")
print("--------------------GAME OVER--------------------")
print('\n')
print("--------------------THANK YOU FOR PLAYING THE NUMBER GUESSING GAME!--------------------")
print('\n')
