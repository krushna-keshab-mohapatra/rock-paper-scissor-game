import random

print("================================")
print("  ROCK PAPER SCISSORS GAME")
print("================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input(
        "\nChoose rock, paper, or scissors: "
    ).lower().strip()

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer's choice:", computer)

    if user == computer:
        print("Result: It's a tie!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    print("\n--- Scoreboard ---")
    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower().strip()

    if play_again != "yes":
        print("\nFinal Score")
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print("Thanks for playing!")
        break