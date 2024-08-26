import random
def number_guessing_game():
    target_number = random.randint(1, 100)
    guess = None
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    while guess != target_number:
        guess = int(input("Enter your guess: "))
        if guess > target_number and guess <= target_number + 10:
            print("Very close guess! Guess a bit lower.")
        elif guess < target_number and guess >= target_number - 10:
            print("Very close guess! Guess a bit higher.")
        elif guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number: {target_number}")
number_guessing_game()
x = input("do you want o play again ? Y/N:")
while x.lower() == "y":
    number_guessing_game()
    x = input("do you want o play again ? Y/N:")
print("Thankyou! for playing")