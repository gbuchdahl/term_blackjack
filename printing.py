import typing
from typing import List
from card import Card


def print_piles(cards: List[Card]) -> None:
    """ prints a 1D array of cards as they would be a hand"""
    for i in range(len(cards)):
        print("+---+", end=" ")
    print()

    for card in cards:
        num = card.get_name()
        if num == "10":
            print(f"|{num}", end="")
        else:
            print(f"| {num}", end="")
        print(f"{card.get_suit()}|", end=" ")
    print()
    for i in range(len(cards)):
        print("|   |", end=" ")
    print()
    for i in range(len(cards)):
        print("+---+", end=" ")
    print()


if __name__ == "__main__":
    x = [Card(a, "c") for a in range(1, 4)]
    print_piles(x)
