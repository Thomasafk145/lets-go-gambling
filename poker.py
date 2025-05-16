import random
from collections import Counter

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_values = {r: i for i, r in enumerate(ranks, 2)}

# Create deck


def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]

# Deal cards


def deal_hand(deck, num=2):
    return [deck.pop() for _ in range(num)]


def deal_community_cards(deck, num):
    return [deck.pop() for _ in range(num)]

# Display hand


def display_hand(hand):
    return ', '.join([f"{rank} of {suit}" for rank, suit in hand])

# Evaluate hand strength (simple score based on ranks)


def hand_score(hand):
    ranks_only = [rank for rank, _ in hand]
    rank_counts = Counter(ranks_only)
    most_common = rank_counts.most_common(1)[0][1]

    if most_common == 4:
        return (7, "Four of a Kind")
    elif most_common == 3:
        if len(rank_counts) == 2:
            return (6, "Full House")
        return (3, "Three of a Kind")
    elif most_common == 2:
        if list(rank_counts.values()).count(2) == 2:
            return (2, "Two Pair")
        return (1, "One Pair")
    return (0, "High Card")

# Bot betting strategy (without revealing bluffing)


def bot_bet_decision(hand, current_bet, bot_name, bot_money):
    score, _ = hand_score(hand)
    bluff_chance = random.random()

    if score >= 6:
        raise_amt = min(current_bet + 10, bot_money)
        return raise_amt
    elif score >= 3:
        return min(current_bet, bot_money)
    elif score >= 1:
        if bluff_chance > 0.7:
            raise_amt = min(current_bet + 5, bot_money)
            return raise_amt
        return min(current_bet, bot_money)
    else:
        if bluff_chance > 0.85:
            raise_amt = min(current_bet + 15, bot_money)
            return raise_amt
        elif bluff_chance < 0.2:
            return 0  # Fold
        return min(current_bet, bot_money)

# Combine hand and community cards


def best_hand_score(hand, community):
    combined = hand + community
    return hand_score(combined)

# Player betting input with validation


def player_bet_input(current_money, phase):
    while True:
        try:
            bet = int(input(f"{phase} - Enter your bet (0 to check/fold): $"))
            if 0 <= bet <= current_money:
                return bet
            else:
                print("Invalid amount. Try again.")
        except ValueError:
            print("Enter a valid number.")

# Game setup for Texas Hold'em style poker


def play_poker():
    player_money = 100
    bot1_money = 100
    bot2_money = 100

    while player_money > 0:
        print(f"\nYou have ${player_money} to start this round.")

        deck = create_deck()
        random.shuffle(deck)

        player_hand = deal_hand(deck)
        bot1_hand = deal_hand(deck)
        bot2_hand = deal_hand(deck)

        print("\nYour hand:", display_hand(player_hand))

        pot = 0
        side_pots = []  # List to hold side pots
        all_bets = {}  # Track the total bets for each player

        # Pre-Flop Betting
        bet = player_bet_input(player_money, "Pre-Flop")
        player_money -= bet
        all_bets['You'] = bet
        pot += bet

        bot1_bet = bot_bet_decision(bot1_hand, bet, "Bot 1", bot1_money)
        bot2_bet = bot_bet_decision(bot2_hand, bet, "Bot 2", bot2_money)
        bot1_money -= bot1_bet
        bot2_money -= bot2_bet
        all_bets['Bot 1'] = bot1_bet
        all_bets['Bot 2'] = bot2_bet
        pot += bot1_bet + bot2_bet

        # Flop
        community_cards = deal_community_cards(deck, 3)
        print("\nFlop:", display_hand(community_cards))

        # Flop Betting
        bet = player_bet_input(player_money, "Flop")
        player_money -= bet
        all_bets['You'] += bet
        pot += bet

        bot1_bet = bot_bet_decision(
            bot1_hand + community_cards, bet, "Bot 1", bot1_money)
        bot2_bet = bot_bet_decision(
            bot2_hand + community_cards, bet, "Bot 2", bot2_money)
        bot1_money -= bot1_bet
        bot2_money -= bot2_bet
        all_bets['Bot 1'] += bot1_bet
        all_bets['Bot 2'] += bot2_bet
        pot += bot1_bet + bot2_bet

        # Turn
        community_cards += deal_community_cards(deck, 1)
        print("Turn:", display_hand([community_cards[3]]))

        # Turn Betting
        bet = player_bet_input(player_money, "Turn")
        player_money -= bet
        all_bets['You'] += bet
        pot += bet

        bot1_bet = bot_bet_decision(
            bot1_hand + community_cards, bet, "Bot 1", bot1_money)
        bot2_bet = bot_bet_decision(
            bot2_hand + community_cards, bet, "Bot 2", bot2_money)
        bot1_money -= bot1_bet
        bot2_money -= bot2_bet
        all_bets['Bot 1'] += bot1_bet
        all_bets['Bot 2'] += bot2_bet
        pot += bot1_bet + bot2_bet

        # River
        community_cards += deal_community_cards(deck, 1)
        print("River:", display_hand([community_cards[4]]))

        # River Betting
        bet = player_bet_input(player_money, "River")
        player_money -= bet
        all_bets['You'] += bet
        pot += bet

        bot1_bet = bot_bet_decision(
            bot1_hand + community_cards, bet, "Bot 1", bot1_money)
        bot2_bet = bot_bet_decision(
            bot2_hand + community_cards, bet, "Bot 2", bot2_money)
        bot1_money -= bot1_bet
        bot2_money -= bot2_bet
        all_bets['Bot 1'] += bot1_bet
        all_bets['Bot 2'] += bot2_bet
        pot += bot1_bet + bot2_bet

        # Calculate side pots
        all_bets_sorted = sorted(
            all_bets.items(), key=lambda x: x[1], reverse=True)
        highest_bet = all_bets_sorted[0][1]
        side_pot = 0
        for player, bet in all_bets_sorted:
            if bet < highest_bet:
                side_pots.append((player, highest_bet - bet))
                highest_bet = bet

        # Evaluate hands
        player_score = best_hand_score(player_hand, community_cards)
        bot1_score = best_hand_score(
            bot1_hand, community_cards) if all_bets['Bot 1'] > 0 else (-1, "Folded")
        bot2_score = best_hand_score(
            bot2_hand, community_cards) if all_bets['Bot 2'] > 0 else (-1, "Folded")

        if all_bets['Bot 1'] > 0:
            print("\nBot 1 hand:", display_hand(bot1_hand))
            print("Bot 1 has:", bot1_score[1])
        else:
            print("\nBot 1 folded.")

        if all_bets['Bot 2'] > 0:
            print("\nBot 2 hand:", display_hand(bot2_hand))
            print("Bot 2 has:", bot2_score[1])
        else:
            print("\nBot 2 folded.")

        all_scores = [("You", player_score)]
        if all_bets['Bot 1'] > 0:
            all_scores.append(("Bot 1", bot1_score))
        if all_bets['Bot 2'] > 0:
            all_scores.append(("Bot 2", bot2_score))

        winner = max(all_scores, key=lambda x: x[1][0])
        print(f"\nWinner: {winner[0]} with a {winner[1][1]}!")

        if winner[0] == "You":
            player_money += pot
            print(f"You win the main pot! You now have ${player_money}.")
        else:
            print(f"You lost your bets. You now have ${player_money}.")

        # Handle side pots
        for side_player, side_bet in side_pots:
            print(f"{side_player} won a side pot of ${side_bet}!")

        if player_money <= 0:
            print("\nYou are out of money. Game over!")
            break

        again = input("\nPlay another round? (y/n): ").lower()
        if again != 'y':
            break


if __name__ == "__main__":
    play_poker()
