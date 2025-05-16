import random

money = 100


def show_rules():
    print("\n--- Horse Race Rules ---")
    print("1. Choose how much money you want to bet.")
    print("2. Pick a horse between 1 and 8.")
    print("3. If your horse wins, you earn 1.5x your bet!")
    print("4. If you lose, you lose your bet amount.")
    print("5. Type 'all' to bet all your money.")
    print("6. Type 'rules' at the bet prompt to view these rules again.")
    print("-------------------------\n")


def run():
    global money
    print("Time for a horse race!")

    while money > 0:
        print(f"\nYou have ${money}")

        bet_input = input(
            "How much money do you want to bet? (type 'all' or 'rules'): ").lower().strip()
        if bet_input == "rules":
            show_rules()
            continue
        elif bet_input == "all":
            bet = money
            print(f"Going all-in with ${bet}!")
        else:
            try:
                bet = int(bet_input)
                if bet <= 0:
                    print("You must bet a positive amount!")
                    continue
                if bet > money:
                    print("You don't have enough to bet that much!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number, 'all', or 'rules'.")
                continue

        guess = input("Which horse will win? (1-8): ").strip()
        if not guess.isdigit() or not (1 <= int(guess) <= 8):
            print("Invalid horse number! Choose between 1 and 8.")
            continue
        guess = int(guess)

        horse = random.randint(1, 8)
        print(f"Number {horse} has won!")

        if guess == horse:
            winnings = int(bet * 1.5)
            print(f"You have earned ${winnings}!")
            money += winnings
        else:
            money -= bet
            print(f"Wrong guess. You lost ${bet}.")

        print(f"You now have ${money} remaining.")

        if money > 0:
            again = input(
                "Would you like to play again? (y/n): ").lower().strip()
            if again != "y":
                print("You're no fun! Bye!")
                break
        else:
            print("You're out of money! Game over.")


if __name__ == "__main__":
    run()
