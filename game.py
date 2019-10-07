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
        # We stop when you're out of money
        if player.get_money() <= 0:
            break

        # Make a clean screen, show player info
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---\n")
        print(player)
        print("\n---")

        # get the bet amount
        player.set_bet(
            int(
                cutie.get_number(
                    "What bet would you like to make?", 0, player.get_money()
                )
            )
        )
        player.change_money(0 - player.get_bet())

        # Hand should now be two cards
        player.reset_hand()
        for i in range(2):
            card, deck = draw(deck)
            player.add_to_hand(card)
        player.print_hand()

        flag = True
        busted = False
        while flag:
            # Hit and stick become two options in the terminal
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

            # Bust if sum > 21
            if player.sum_hand() > 21:
                print("Over 21! You're busted.")
                busted = True
                flag = False

        # if the player stuck, and didn't bust, the dealer goes
        if not busted:
            dealer_bust = False

            # print dealer information
            print("---\n")
            print("Dealer:")
            print("\n---")
            dealer.reset_hand()
            for i in range(2):
                card, deck = draw(deck)
                dealer.add_to_hand(card)
            dealer.print_hand()

            # the wait makes it feel more human
            time.sleep(1)

            # dealers hit on 16, stick on 17
            while dealer.sum_hand() < 17:
                print("Dealer hits.\n")
                card, deck = draw(deck)
                dealer.add_to_hand(card)
                dealer.print_hand()
                time.sleep(1)

            # the dealer can bust too
            if dealer.sum_hand() > 21:
                print("Dealer busts!")
                dealer_bust = True
            else:
                print("Dealer Sticks.")

            # Victory logic
            # using the getters to avoid making more variables

            # tie geets your money back
            if player.sum_hand() == dealer.sum_hand() and player.sum_hand() <= 21:
                print(f"{player.get_name()} ties.")
                player.change_money(player.get_bet())
                player.set_bet(0)

            # beating the dealer gets the bet won
            elif (
                dealer_bust
                or player.sum_hand() > dealer.sum_hand()
                and player.sum_hand() < 21
            ):
                print(f"{player.get_name()} wins!")
                player.change_money(2 * player.get_bet())
                player.set_bet(0)

            # blackjack pays 3/2, but that's only Ace and a Face card
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

    final_money = player.get_money()
    if final_money < 500:
        print(f"You ended up losing {500-final_money} dollars.")
    elif final_money == 500:
        print("You broke even!")
    else:
        print(f"You won {final_money-500} dollars!")


# returns the deck and the top card, resetting if need be
def draw(deck):
    if deck == None or deck == []:
        deck = reset_deck()
    card = deck.pop()
    return card, deck


# puts all the cards into the deck and then shuffles it
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
