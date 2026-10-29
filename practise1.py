import random
jackpot=random.randint(1,100)
guess=int(input("Guess a number between 1 and 100: "))
while guess!=jackpot:
    if guess<jackpot:
        print("Low guess, try again.")
    elif guess>jackpot:
        print("High guess, try again.")
    guess=int(input("Guess a number between 1 and 100: "))
if guess==jackpot:
    print("Congratulations! You guessed the jackpot number:", jackpot)
    

