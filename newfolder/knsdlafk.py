import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100 (inclusive): "))
            attempts += 1
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
if __name__ == "__main__":
    guess_number()