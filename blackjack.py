import random

# Constants
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = list(CARD_VALUES.keys())


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def get_value(self):
        return CARD_VALUES[self.rank]


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = sum(card.get_value() for card in self.cards)
        # Adjust for Aces
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


def main():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Initial dealing
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    print("Player's Hand:", player_hand)
    print("Dealer's Hand: [", dealer_hand.cards[0], ", ?]")

    # Player's turn
    while True:
        choice = input("Do you want to (h)it or (s)tand? ").lower()
        if choice == 'h':
            player_hand.add_card(deck.deal_card())
            print("Player's Hand:", player_hand)
            if player_hand.get_value() > 21:
                print("Bust! You lose.")
                return
        elif choice == 's':
            break

    # Dealer's turn
    print("Dealer's Hand:", dealer_hand)
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        print("Dealer's Hand:", dealer_hand)

    # Determine the outcome
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    print(f"Player's Total: {player_value}, Dealer's Total: {dealer_value}")

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
