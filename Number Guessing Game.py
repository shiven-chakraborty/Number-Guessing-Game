import random

playing = input("Do you want to start? Type Y or N (Yes/No). ")

if playing.lower() == "n":
    print("Okay, You can run the game again anytime you want to play!")
    quit()

elif playing.lower() == "y":
    print("Okay, Let's start this game!!")
else:
    print("Kindly enter a valid entry!")

    quit()
print()

number = input("Type a number: ")

if number.isdigit():
    number = int(number)

    if number <= 0: 
        print("Please type a number larger than 0 next time!")
        quit()
else: 
    print("Kindly type a number next time.")

random_number = random.randint(1, number)
guesses = 0

while True:
    guesses += 1
    print()
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
        print("Incorrect Guess. Try again")
        
        if user_guess > number:
            print("Your guess is bigger than the initial number")

        elif user_guess > random_number:
            print("The number you guessed was greater than the number generated")
            print()

        else:
            print("The number you guessed was lesser than the number generated")
            print()

print()
print("You got the correct answer in", guesses, "guess(s)")