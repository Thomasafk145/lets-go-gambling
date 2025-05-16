import random

money = 100
jackpot = 500
lucky_mode = False

sym = ["🍒", "🍋", "🍉", "🔔", "⭐", "💎", "7️⃣",
       "🍀", "👑", "🔥", "🐯", "🪙", "🃏", "🛸", "🧨"]


def weighted_random():
    """Returns a symbol index with increased 7️⃣ chance if lucky_mode is on."""
    if lucky_mode:
        weights = [1]*5 + [1, 5] + [1]*(15-7)  # Boost weight for 7️⃣ (index 6)
        return random.choices(range(15), weights=weights)[0]
    else:
        return random.randint(0, 14)


def handle_triple_symbol_effect(num):
    global money, lucky_mode

    if num <= 4:
        return

    if num == 5:  # 💎
        print("💎 Triple Diamonds! You win $20.")
        money += 30

    elif num == 6:  # 7️⃣
        print("7️⃣ JACKPOT!!! You win $500!")
        money += jackpot

    elif num == 7:  # 🍀
        print("🍀 Lucky triple! Jackpot odds increased.")
        lucky_mode = True

    elif num == 8:  # 👑
        print("👑 Triple Crown! You gain $100.")
        money += 100

    elif num == 10:  # 🐯
        print("🐯 Tiger Trio! You lose $15.")
        money -= 15

    elif num == 11:  # 🪙
        print("🪙 Triple Coin! You win $50.")
        money += 50

    elif num == 12:  # 🃏
        print("🃏 Joker triple! Random effect...")
        if random.choice([True, False]):
            print("Lucky you! You gain $80.")
            money += 80
        else:
            print("Oh no! You lose $100.")
            money -= 100

    elif num == 13:  # 🛸
        print("🛸 Triple Warp! All slots reshuffled.")
        return "warp"


def spin():
    global money

    while money > 0:
        while True:
            num1 = weighted_random()
            num2 = weighted_random()
            num3 = weighted_random()

            if num1 == 9:
                print("🔥 Fire on slot 1! Rerolling...")
                num1 = weighted_random()
            if num2 == 9:
                print("🔥 Fire on slot 2! Rerolling...")
                num2 = weighted_random()
            if num3 == 9:
                print("🔥 Fire on slot 3! Rerolling...")
                num3 = weighted_random()

            print(f"\n{sym[num1]} {sym[num2]} {sym[num3]}")

            if 14 in [num1, num2, num3]:
                print("🧨 Bomb triggered! Rerolling all slots...")
                continue

            if num1 == num2 == num3:
                result = handle_triple_symbol_effect(num1)
                if result == "warp":
                    print("🔁 Warping! Rerolling again...")
                    continue
                print("✨ Triple match! Bonus $30!")
                money += 20
            else:
                print("No triple match this time!")

            break

        money -= 5
        print(f"You have ${money}")

        if money <= 0:
            print("You're broke! GET OUT!!!.")
            break

        user_in = input("Play again? (y/n): ").lower().strip()
        if user_in != "y":
            print("You're no fun!")
            break


if __name__ == "__main__":
    play = input("Would you like to play the slots? (y/n): ").lower().strip()
    if play == "y":
        spin()
    else:
        print("You're no fun!")
