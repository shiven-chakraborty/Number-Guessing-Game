import random

playing = input("Do you want to start this awesome game? Type Yes or No. ")

if playing.lower() != "yes":
    print("Okay, You can run the game again anytime you want to play!")
    quit()

print("Okay then, Let's start this game!!")

print()

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print("Please type a number larger than 0 next time!")
        quit()
else: 
    print("Kindly type a number next time.")

random_number = random.randint(1, top_of_range)
guesses = 0

print()

while True:
    guesses += 1
    user_guess = input("Make a guess of the number generated: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Kindly type a number next time.")
        continue

    if user_guess == random_number:
        print("Congratulations! You have guessed the number!")
        break
    else: 
        print("Nope :( Guess again!")
        if user_guess > random_number:
            print("(BTW, The number you guessed was greater than the number generated)")
            print()
        else:
            print("(BTW, the number you guessed was lesser than the number generated!)")
            print()

print()
print("You got the correct answer in", guesses, "guesses")