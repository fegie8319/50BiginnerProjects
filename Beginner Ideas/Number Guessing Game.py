# Develop a number guessing game. The computer comes up with a random number and you can make guesses. It then tells you if the secret number is greater or smaller. At the end it tells you how many attempts you needed.
import random

com_num = random.randint(1,101)

while True:
    user_input = input("Please enter an integer from 1 to 100: ")
    user_in = int(user_input)
    if user_in < com_num:
        print("It's smaller than the answer!")

    elif user_in > com_num:
        print("It's bigger than the answer!")

    else:
        print("Congratulations!")
        break
