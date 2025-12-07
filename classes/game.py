from classes.deck import Deck
from classes.card import *
from classes.player import Player
from time import sleep
from classes.results import PlayerResult
import os

class Game:

    def __init__(self):
        self.dealer = Player("Dealer", False)
        self.players : list[Player] = []
        self.deck = Deck()
        self.MAX_PLAYERS : int = 6



    def run(self) -> None:

        print(f"Enter number of players.")
        number_of_players = self.__get_number_choice_in_range(1, self.MAX_PLAYERS)

        for i in range(number_of_players):
            self.__add_player(i + 1)

        self.__play_round()
        if self.__blackjack():
            return

        for player in self.players:
            player.result = self.__player_play(player)

        self.dealer.result = self.__dealer_play()

        self.__print_result()



    def __play_round(self) -> None:
        self.deck.shuffle()
        self.__draw_hands()
        self.__print_board(True)



    def __blackjack(self) -> bool:
        for player in self.players:
            if player.has_blackjack():
                if self.dealer.has_blackjack():
                    print("DRAW!")
                else:
                    print(f"{player.name} WINS THE ROUND!")
                return True
        return False
    


    def __dealer_play(self) -> PlayerResult:
        while True:
            self.dealer.calculate_points()
            self.__print_hand(self.dealer)
            if self.dealer.points <= 16:
                self.dealer.take_card(self.deck)
                print("Dealer takes another card!")
            else:
                print("Dealer keeps hand.")
                if self.dealer.points > 21:
                    return PlayerResult.BUST
                if self.dealer.points == 21:
                    return PlayerResult.ON21
                return PlayerResult.BELOW          


    
    def __player_play(self, player : Player) -> PlayerResult:
        while True:
            self.__print_hand(player)
            print(f"--- {player.name}'s turn: ")
            print("1. Hit (Take another card)")
            print("2. Stand (Keep hand)")
            if self.__get_number_choice_in_range(1, 2) == 1:
                player.take_card(self.deck)
                player.calculate_points()
                if player.points == 21:
                    return PlayerResult.ON21
                if player.points > 21:
                    return PlayerResult.BUST
            else:
                return PlayerResult.BELOW
        


    def __get_number_choice_in_range(self, start : int , end : int) -> int:
        while True:
            print(f"Enter a number from {start} to {end}")
            input_str : str = str(input())

            if input_str.isdigit():
                num_input = int(input_str)
                if num_input >= start and num_input <= end:
                    return num_input
            
            print(f"Input must be a valid number between {start} and {end}")


    def __add_player(self, num : int) -> None:
        while True:
            print(f"Enter name for player {str(num)}: ")
            name : str = str(input())

            if len(name) == 0:
                print("Player name can't be empty!")
            elif name.isspace():
                print("Player can't be whitespace!")
            else:
                self.players.append(Player(name))
                break


    
    def __draw_hands(self) -> None:
        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)

        for player in self.players:
            player.take_card(self.deck)
            player.take_card(self.deck)
            player.calculate_points()


    def __print_board(self, initial_round = False) -> None:
        if initial_round:
            print("======= Dealer's hand:")
            print(f"{self.dealer.hand[0].number.value} of {self.dealer.hand[0].type.value}")
            print(f"- hidden -")
            print()
        else:
            self.__print_hand(self.dealer)

        for player in self.players:
            self.__print_hand(player)


    def __print_hand(self, player : Player) -> None:
        print(f"======= {player.name}'s hand:")
        for card in player.hand:
            print(f"{card.number.value} of {card.type.value}")
        if player.has_blackjack():
            print("\tBLACKJACK!")
        else:
            print(f"\tTotal points: {player.points}")
        print()


    def __print_result(self) -> None:
        print()
        print("======= Game Result =======")
        print(f"{self.dealer.name} - {self.dealer.result.value}: {self.dealer.points}")

        max_points = float("-inf")
        winner : Player = None

        if self.dealer.result != PlayerResult.BUST:
            max_points = self.dealer.points
            winner = self.dealer


        for player in self.players:
            print(f"{player.name} - {player.result.value}: {player.points}")
            if player.result != PlayerResult.BUST:
                if player.points > max_points:
                    max_points = player.points
                    winner = player
        
        print(f"{winner.name} WINS THE ROUND!")

        


    def __clear_console(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")