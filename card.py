import typing


class Card:
    def __init__(self, num: int, suit: str):
        self.num = num
        self.suit = suit

    # a function that translates card numbers to names
    def get_name(self) -> str:
        if self.num == 11:
            return "J"
        if self.num == 12:
            return "Q"
        if self.num == 13:
            return "K"
        if self.num == 1:
            return "A"
        else:
            return str(self.num)

    # print a small version of the card
    def print_little(self) -> str:
        return f"+--+\n|{self.get_name()}{self.suit}|"

    # print the card in full
    def __str__(self) -> str:
        str = f"+--+\n|{self.get_name()} |\n| {self.suit}|\n+--+"
        return str


# driver function for testing
if __name__ == "__main__":
    print(Card(12, "c").print_little())
    print(Card(1, "h"))
