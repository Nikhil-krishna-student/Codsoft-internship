import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice")
        return None, None, None
    comp = random.choice(choices)
    if user == comp:
        result = "Tie"
    elif (user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper") or (user == "paper" and comp == "rock"):
        result = "Win"
    else:
        result = "Lose"
    print(f"You chose {user}, computer chose {comp}. Result: {result}")
    return user, comp, result

def main():
    user_score = comp_score = 0
    while True:
        _, _, result = play_round()
        if result == "Win":
            user_score += 1
        elif result == "Lose":
            comp_score += 1
        print(f"Score -> You: {user_score} | Computer: {comp_score}")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break
    print("Final Score -> You:", user_score, "| Computer:", comp_score)

if __name__ == "__main__":
    main()
