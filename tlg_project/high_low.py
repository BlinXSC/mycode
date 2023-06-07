#!/usr/bin/env python3
""" Alan Alegre | High Low Game """

from textwrap import dedent
from playing_card import PlayingCard

def hi_low_game():
    """ Runs the game of high low """

    games_played = 0
    wins = 0
    losses = 0
    ties = 0
    bankroll = 0
    final_bankroll = 0
    answer = 'N'
    player_guess = ''
    corr_guess = ''

    print(dedent("""
        =====================================INSTRUCTIONS============================================
        Welcome to a game of HiLo. This game is played with a 52 card deck. You will be asked
        to provide an initial bankroll. Afterwards, you will be asked to place a bet between
        $0.01 and $100.00. You will be shown one card, and your task is to guess if the next card 
        will be higher or lower in face value. The order of card's face value increases from "Two" to
        "Ace". Depending on your guess, you will gain or lose money according to how much you bet.
        The game continues until you run out of money or decide to quit. 
        """))

    # Ensures the user provides a number greater than 0 for the initial bankroll.
    while bankroll <= 0:
        try:
            bankroll = int(input("Please enter a initial bankroll greater than $0.00: "))
        except ValueError:
            print("Invalid input, need a positive integer.")
        except Exception as err:
            print("Did not expect that:", err)
            print("Please try again")

    print(f"\nInitial Bankroll: ${bankroll}")

    # Runs the game
    while bankroll > 0:

        bet = 0 # Resets the bet

        # Ensures player's bet remains within $0.01 and $100.00, and does not exceed bankroll.
        while (bet < 1 or bet > 100) or bet > bankroll:
            try:
                bet = int(input(dedent("""
                Please enter your bet between $1 and $100, or current bankroll
                if it is less than $100.

                >>> """)))
            except ValueError:
                print("Invalid input, need a positive integer.")
            except Exception as err:
                print("Did not expect that:", err)
                print("Please try again")

        print(f"You bet ${bet}")

        # Player draws first card ,and is shown the card.
        card1 = PlayingCard()
        card1.draw_card()
        print(f"\nFirst card: {card1.to_string()}")

        # Prompts player to guess of the card will be higher or lower.
        player_guess = input("\nWill the next card be lower or higher? (Enter H or L) >>> ").upper()

        while player_guess not in ['H', 'L']: #!= 'H' and player_guess != 'L'
            player_guess = input("Invalid input, please only use characters H or L >>> ").upper()

        # Second non-matching card (face value AND suit) is drawn
        card2 = PlayingCard()
        card2.draw_card()

        # Ensures card will be different
        while card2.is_equals(card1) is True:
            card2.draw_card()

        # Second card is displayed
        print(f"\nSecond card: {card2.to_string()}")

        # Assigns 'H' or 'L' if the second card is higher or lower than the first card.
        if card1.get_face() < card2.get_face():
            corr_guess = 'H'
        elif card1.get_face() > card2.get_face():
            corr_guess = 'L'
        else:
            corr_guess = 'T'

        # Adds or deducts from player's bankroll depending on accuracy, or preserves bankroll if the
        # card face values are the same. Keeps track of ties, wins, and losses.
        if corr_guess == 'T':
            print("\nCards have the same face value, tie game.")
            ties += 1
        elif player_guess == corr_guess:
            print("\nCorrect!!! You Win!!!")
            bankroll += bet
            wins += 1
        elif player_guess != corr_guess:
            print("\nIncorrect, please try again...")
            bankroll -= bet
            losses += 1

        # Keeps track of how many games were played
        games_played += 1

        # Display current bankroll
        print(f"\nCurrent Bankroll: ${bankroll}")

        # Ask player if they wish to continue if bankroll is greater than zero.
        if bankroll > 0:
            answer = input("\nDo you wish to continue (Y or N)? >>> ").upper()

        # Ensures only 'Y' or N' will be accepted for the previous question.
        while answer not in ['Y', 'N']:
            answer = input("Invalid input, please only user characters 'Y' or 'N' >>> ").upper()

        # Ends the game and saves final bankroll upon player request.
        if answer == 'N' and bankroll > 0:
            final_bankroll = bankroll
            bankroll -= bankroll

    # Prints results
    print(dedent(f"""
        Total Number of Games Played: {games_played}
        Total Number of Wins: {wins}
        Total Number of Losses: {losses}
        Total Number of Ties: {ties}
        """))


    if final_bankroll > 0:
        print(f"Final Bankroll: ${final_bankroll}")
    else:
        print("Best you stay out of Vegas...")

    print("\nReturning to Game Box...")

def main():
    """ Main runtime function """
    hi_low_game()

if __name__ == "__main__":
    main()
