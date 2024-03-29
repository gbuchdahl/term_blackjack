from card import Card
from printing import print_piles


class Player:
    """ a class that stores the player information"""

    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.money = 500
        self.bet = 0

    def set_bet(self, val: int):
        self.bet = val

    def get_bet(self):
        return self.bet

    def get_hand(self):
        return self.hand

    def add_to_hand(self, card: Card):
        self.hand.append(card)
        return

    def reset_hand(self):
        self.hand = []

    def print_hand(self):
        print_piles(self.hand)
        print(f"Sum: {self.sum_hand()}")
        return None

    def sum_hand(self):
        # in general, we want to sum the values of the cards
        # some of the cards are worth 10 even though they arent tens
        # aces are conditionally worth 1 or 11
        res = 0
        aces = 0
        for card in self.hand:
            res += card.get_value()
            if card.get_name() == "A":
                aces += 1

        # ace logic
        while aces and res > 21:
            aces -= 1
            res -= 10

        return res

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def change_money(self, amount: int):
        self.money += amount
        return None

    def __str__(self):
        return f"Name: {self.get_name()}\nCash: {self.get_money()}"
