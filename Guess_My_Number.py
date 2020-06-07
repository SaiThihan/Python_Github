#Challenge 19:Guess My number App

#import random lib
import random
#Welcome message of Guess my number
print("Welcome to the Guess My Number App")

#Gather user input
name=input("Hello!What is your name: ")
print("Well " + name + " I am thinking of a number between 1 and 20")

number =random.randint(1,20)

for guess_num in range(5): #use guess_num to use frequency
    guess=int(input("\nTake a guess: "))  #use as input guess num every single looping

    if guess<number:
        print("Your guess is too low.")
    elif guess>number:
        print("Your guess is to high.")
    else:
        break

if guess==number:
    print("\nGood job, " + name + "! You guessed my number in " + str(guess_num+1) + "guesses!")
else:
    print("\nGame Over,The number I was thinking of was " + str(number) + ".")
