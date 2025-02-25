import random

def get_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    
    if (user == "snake" and computer == "water") or \
       (user == "water" and computer == "gun") or \
       (user == "gun" and computer == "snake"):
        return "You Win! 🎉"
    
    return "You Lose! 😢"

# Choices
options = ["snake", "water", "gun"]

# Game Loop
while True:
    print("\nChoose: Snake 🐍, Water 💧, or Gun 🔫 (or type 'exit' to quit)")
    user_choice = input("Your choice: ").strip().lower()

    if user_choice == "exit":
        print("Thanks for playing! 🎮")
        break
    
    if user_choice not in options:
        print("Invalid choice! Please select snake, water, or gun.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)
