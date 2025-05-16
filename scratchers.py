import random
import time

card_cost = 10
STARTING_BALANCE = 100
JACKPOT_REWARD = 1_000_000
SMALL_PRIZE = random.randint(10, 30)
IMPOSSIBLE_ODDS = 10**20
SMALL_JACKPOT = random.randint(100,5000)

SYMBOLS = ['🍒', '🍋', '🔔', '⭐', '💎', '🍀', '🎲', '🎯', '🥇', '🪙']


class Player:
    def __init__(self, name, balance=STARTING_BALANCE):
        self.name = name
        self.balance = balance
        self.total_spent = 0
        self.games_played = 0
        self.jackpots_won = 0
        self.small_wins = 0

    def can_play(self, num_cards=1):
        return self.balance >= card_cost * num_cards

    def deduct(self, num_cards):
        cost = card_cost * num_cards
        self.balance -= cost
        self.total_spent += cost
        self.games_played += num_cards

    def add_jackpot(self):
        self.balance += JACKPOT_REWARD
        self.jackpots_won += 1

    def add_small_jackpot(self):
        self.balance += SMALL_JACKPOT
        self.jackpots_won += 1

    def add_small_prize(self):
        self.balance += SMALL_PRIZE
        self.small_wins += 1

    def top_up(self, amount):
        self.balance += amount

    def stats(self):
        return f"""
        👤 Player: {self.name}
        💰 Balance: ${self.balance}
        🎮 Games Played: {self.games_played}
        🧾 Total Spent: ${self.total_spent}
        🏆 Jackpots (includes small jackpot): {self.jackpots_won}
        💸 Small Wins: {self.small_wins}
        """


class ScratchCardGame:
    def __init__(self, player):
        self.player = player

    def draw_symbols(self):
        return [random.choice(SYMBOLS) for _ in range(3)]

    def display_symbols(self, symbols):
        for i in range(3):
            time.sleep(0.5)
            print(f"[ {symbols[i]} ]", end=" ", flush=True)
        print("\n")

    def check_result(self, symbols):
        if symbols[0] == symbols[1] == symbols[2]:
            if random.randint(1, IMPOSSIBLE_ODDS) == 1:
                self.player.add_jackpot()
                print(
                    f"\n🎉 SMALL JACKPOT!!! You matched 3 {symbols[0]}s and got the winning number, winning ${JACKPOT_REWARD:,}!")
                return "jackpot"
            else:
                self.player.add_small_jackpot()
                print(
                    f"\n🎉 JACKPOT!!! You matched 3 {symbols[0]}s and won ${SMALL_JACKPOT:,}!")
                return "small jackpot"
        if symbols[0] == symbols[1] or symbols[1] == symbols[2] or symbols[0] == symbols[2]:
            self.player.add_small_prize()
            print(
                f"\n✨ Small win! You matched 2 symbols and won ${SMALL_PRIZE}.")
            return "small_win"
        print("😢 No match. Better luck next time.")
        return "no_win"

    def play_batch(self, num_cards):
        self.player.deduct(num_cards)
        print(f"\n🎟️ Scratching {num_cards} card(s)...\n")

        for i in range(1, num_cards + 1):
            print(f"🪙 Card #{i}")
            symbols = self.draw_symbols()
            self.display_symbols(symbols)
            self.check_result(symbols)
            print(f"💵 Balance: ${self.player.balance}\n")
            time.sleep(0.5)

    def ask_continue(self):
        return input("Play again? (y/n): ").strip().lower() == 'y'

    def ask_top_up(self,):

        choice = input(
            "Would you like to top up your balance? (y/n): ").strip().lower()
        if choice == 'y':
            while True:
                try:
                    amount = int(input("Enter top-up amount: $"))
                    if amount > 900:
                        card_cost = amount
                        self.player.top_up(amount)
                        print(
                            f"✅ Balance topped up! New balance: ${self.player.balance}")
                        return card_cost

                    elif amount > 0:
                        self.player.top_up(amount)
                        print(
                            f"✅ Balance topped up! New balance: ${self.player.balance}")
                        break

                except ValueError:
                    print("Please enter a valid number.")


def main():
    print("🎰 Welcome to the ULTIMATE Scratch Card Game, Where The Big Jackpot Needs 3 Matching Symbols And The Lucky Number 🎰")
    name = input("Enter your name: ").strip() or "Player 1"
    player = Player(name)
    game = ScratchCardGame(player)

    while True:
        print(f"\n💰 Your current balance: ${player.balance}")
        try:
            num = int(
                input(f"How many scratchers do you want to buy? (${card_cost} each): "))
            if num <= 0:
                print("🚫 Please enter a number greater than 0.")
                continue
            if not player.can_play(num):
                print(
                    f"❌ You don't have enough money to buy {num} scratcher(s).")
                game.ask_top_up()
                continue
            game.play_batch(num)
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")
            continue

        if not game.ask_continue():
            break

    print("\n📊 Game Summary:")
    print(player.stats())
    print("👋 Thanks for playing!")


if __name__ == "__main__":
    main()
