import random

user_win = 0
computer_win = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    # 0, 1, 2 = rock, paper, scissors
    computer_input = ["rock", "paper", "scissors"][random_number]

    print(f"Computer chose {computer_input}.")

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        user_win += 1
    else:
        print("You lose!")
        computer_win += 1 

print(f"Score: You {user_win} - Computer {computer_win}")
print("Thanks for playing!")