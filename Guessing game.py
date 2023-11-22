import random

def guessing_game():
    print("Hey Welcome!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        user_input = input("Take a guess (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print(f"The number was {secret_number}. Thanks for playing!")
            break
        try:
            user_guess = int(user_input)
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")

guessing_game()
