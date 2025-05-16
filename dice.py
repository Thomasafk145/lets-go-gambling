import random


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll = die1 + die2
    print(f"You rolled {die1} + {die2} = {roll}")
    return roll


def show_rules():
    print("\n--- Craps Rules ---")
    print("1. You roll two dice.")
    print("2. On the first roll:")
    print("   - Rolling a 7 or 11 wins.")
    print("   - Rolling a 2, 3, or 12 loses (called 'Craps').")
    print("   - Any other number becomes your 'Point'.")
    print("3. If you set a Point, keep rolling:")
    print("   - Rolling the Point again wins.")
    print("   - Rolling a 7 before the Point loses.")
    print("4. You can bet any amount or type 'all' to bet everything.")
    print("---------------------\n")


def get_bet(balance):
    while True:
        bet_input = input(
            f"How much would you like to bet? (Available: ${balance}) (type 'all' or 'rules'): ").strip().lower()
        if bet_input == 'all':
            print(f"Going all-in with ${balance}!")
            return balance
        elif bet_input == 'rules':
            show_rules()
            continue
        try:
            bet = int(bet_input)
            if 1 <= bet <= balance:
                return bet
            else:
                print(f"Invalid bet. Bet must be between $1 and ${balance}.")
        except ValueError:
            print("Please enter a valid number, 'all', or 'rules'.")


def play_craps():
    balance = 100
    print("Welcome to Craps!")
    print(f"You are starting with ${balance}.")

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        bet = get_bet(balance)
        first_roll = roll_dice()

        if first_roll in (7, 11):
            print("You win!")
            balance += bet
            print(f"Your current balance is ${balance}")
        elif first_roll in (2, 3, 12):
            print("Craps! You lose.")
            balance -= bet
            print(f"Your current balance is ${balance}")
        else:
            point = first_roll
            print(f"Point is set to {point}. Keep rolling!")

            while True:
                roll = roll_dice()
                if roll == point:
                    print("You made your point! You win!")
                    balance += bet
                    print(f"Your current balance is ${balance}")
                    break
                elif roll == 7:
                    print("You rolled a 7. You lose.")
                    balance -= bet
                    break

        if balance > 0:
            keep_playing = input(
                "\nDo you want to keep playing? (y/n): ").strip().lower()
            if keep_playing != 'y':
                break
        else:
            print("You're out of money! Game over.")

    print(f"\nYou finished with ${balance}. Thanks for playing!")


if __name__ == "__main__":
    play_craps()
