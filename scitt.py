"""  Please make sure you read the entire README.md file to follow the instructions. 
You dont have to follow how I have started the game. Please use your creativity """

# print("Welcome to the Number Guessing Game!")
# pass
welcome_txt = """
                Hey! Welcome to the guessing game...
                It's a simple game where you try and guess an existing number from a range of numbers
                Here are the instructions:
                A number has already been set in a range of 1 to 10
                As a user you are required to input a number which you think is the set number
                You do this until you get the correct number
            """
print(welcome_txt)
import random

random_number = random.randint(1, 10)
print(f"The selected number is:{random_number}")
while random_number:

    guessed_number = int(input("Enter a number that you think is set(should be in the range of 1 to 10):"))
    print(f"Just to ascertain, your number is {guessed_number}")
    if guessed_number == random_number:
        print("Congratulations!! You guessed the correct number")
        break
    elif guessed_number > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

