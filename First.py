import random

n= random.randint(1,10)

print("I am thinking of a number between 1 and 10, Guess the number")

running = True

while running:
    guess_str = input("Guess the number between 1 and 10")
    guess = int(guess_str)
    if(guess == n):
        print("Well done !! you have guessed it right")
        running = False
    elif(guess < n):
        print("guess a higher number")
    else:
        print("guess a lower number")


