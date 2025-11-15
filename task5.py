import random

# Define valid choices
choices = {'rock', 'paper', 'scissors'}

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(list(choices))
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)