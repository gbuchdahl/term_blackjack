import cutie
import random
import copy
import time
from player import Player
from card import Card


def main():
    # start the game off
    print("What is your name: ", end="")
    name = input()
    player = Player(name)
    dealer = Player("Dealer")
    deck = reset_deck()
    game = True

    while game:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---\n")
        print(player)
        print("\n---")
        player.set_bet(int(cutie.get_number("What bet would you like to make?", 0)))
        player.change_money(0 - player.get_bet())

        player.reset_hand()
        for i in range(2):
            card, deck = draw(deck)
            player.add_to_hand(card)
        player.print_hand()

        flag = True
        busted = False
        while flag:
            print("\n~Use the arrow keys and enter to select~\n")
            opts = ["Hit", "Stick"]
            opt = cutie.select(opts)
            if opt == 1:
                print(f"Hand sum: {player.sum_hand()}")
                flag = False
            if opt == 0:
                card, deck = draw(deck)
                player.add_to_hand(card)
                player.print_hand()

            if player.sum_hand() > 21:
                print("Over 21! You're busted.")
                busted = True
                flag = False

        if not busted:
            dealer_bust = False
            print("---\n")
            print("Dealer:")
            print("\n---")
            dealer.reset_hand()
            for i in range(2):
                card, deck = draw(deck)
                dealer.add_to_hand(card)
            dealer.print_hand()
            time.sleep(1)
            while dealer.sum_hand() < 17:
                print("Dealer hits.\n")
                card, deck = draw(deck)
                dealer.add_to_hand(card)
                dealer.print_hand()
                time.sleep(1)

            if dealer.sum_hand() > 21:
                print("Dealer busts!")
                dealer_bust = True
            else:
                print("Dealer Sticks.")

            if player.sum_hand() == dealer.sum_hand() and player.sum_hand() <= 21:
                print(f"{player.get_name()} ties.")
                player.change_money(player.get_bet())
                player.set_bet(0)
            elif (
                dealer_bust
                or player.sum_hand() > dealer.sum_hand()
                and player.sum_hand() < 21
            ):
                print(f"{player.get_name()} wins!")
                player.change_money(2 * player.get_bet())
                player.set_bet(0)
            elif player.sum_hand() > dealer.sum_hand() and player.sum_hand() == 21:
                hand = player.get_hand()
                if len(hand) == 2 and ("A" in hand):
                    print(f"BLACKJACK!")
                    player.change_money(2 * player.get_bet())
                    player.change_money(0.5 * player.get_bet())
                else:
                    print(f"{player.get_name()} wins!")
                    player.change_money(2 * player.get_bet())
                player.set_bet(0)

            else:
                print(f"{player.get_name()} loses :(")

        opts = ["Continue", "Exit"]
        opt = cutie.select(opts)
        if opt == 1:
            game = False


def draw(deck):
    if deck == None or deck == []:
        deck = reset_deck()
    card = deck.pop()
    return card, deck


def reset_deck():
    deck = []
    suits = ["C", "H", "S", "D"]
    for i in range(1, 14):
        for suit in suits:
            deck.append(Card(i, suit))
    random.shuffle(deck)
    return deck


if __name__ == "__main__":
    main()
