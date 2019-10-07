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
        res = 0
        ace = False
        for card in self.hand:
            res += card.get_value()
            if card.get_name == "A":
                ace = True
        if ace and res > 21:
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
