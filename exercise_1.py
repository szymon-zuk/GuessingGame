import random

# I pick a random number in range(1, 100)
random_number = random.randint(1, 100)

# I assign input to a variable "guessed_number"
guessed_number = input("Guess the number: ")

# I make a loop that keeps going until guessed_number isn't equal to random_number.
while guessed_number != random_number:
    try:
        if int(guessed_number) < random_number:
            print("Too small!")
            guessed_number = input("Guess the number: ")
        elif int(guessed_number) > random_number:
            print("Too big!")
            guessed_number = input("Guess the number: ")
        else:
            break
    except ValueError:
        print("It's not a number!")
        guessed_number = input("Guess the number: ")
print("You win!")
