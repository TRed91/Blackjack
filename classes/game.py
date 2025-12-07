from classes.deck import Deck
from classes.card import *
from classes.player import Player
from classes.results import PlayerResult
from classes.io_factory import IO_Factory, ConsoleIO, IO_Interface
import os

class Game:

    def __init__(self):
        self.dealer = Player("Dealer", False)
        self.players : list[Player] = []
        self.deck = Deck()
        self.MAX_PLAYERS : int = 6
        self.__io : IO_Interface = IO_Factory.get_console_io()


    def run(self) -> None:

        number_of_players = self.__io.get_number_input(1, self.MAX_PLAYERS, "Enter number of players")

        for i in range(number_of_players):
            name = self.__io.get_string_input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(name))

        self.__play_initial_round()
        if self.__blackjack():
            return

        for player in self.players:
            player.result = self.__player_play(player)

        self.dealer.result = self.__dealer_play()

        self.__io.print_result(self.players, self.dealer)



    def __play_initial_round(self) -> None:
        self.deck.shuffle()
        self.__draw_hands()
        self.__io.print_board(self.players, self.dealer, True)



    def __blackjack(self) -> bool:
        for player in self.players:
            if player.has_blackjack():
                if self.dealer.has_blackjack():
                    self.__io.print_info_msg("DRAW!")
                else:
                    self.__io.print_info_msg(f"{player.name} WINS THE ROUND!")
                return True
        return False
    


    def __dealer_play(self) -> PlayerResult:
        while True:
            self.dealer.calculate_points()
            self.__io.print_hand(self.dealer)
            if self.dealer.points <= 16:
                self.dealer.take_card(self.deck)
                self.__io.print_info_msg("Dealer takes another card!")
            else:
                self.__io.print_info_msg("Dealer keeps hand.")
                if self.dealer.points > 21:
                    return PlayerResult.BUST
                if self.dealer.points == 21:
                    return PlayerResult.ON21
                return PlayerResult.BELOW          


    
    def __player_play(self, player : Player) -> PlayerResult:
        while True:
            self.__io.print_hand(player)
            messages = [
                f"--- {player.name}'s turn: ",
                "1. Hit (Take another card)",
                "2. Stand (Keep hand)"
            ]
            self.__io.print_block_msg(messages)
            if self.__io.get_number_input(1, 2, "") == 1:
                player.take_card(self.deck)
                player.calculate_points()
                if player.points == 21:
                    return PlayerResult.ON21
                if player.points > 21:
                    return PlayerResult.BUST
            else:
                return PlayerResult.BELOW


    
    def __draw_hands(self) -> None:
        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)

        for player in self.players:
            player.take_card(self.deck)
            player.take_card(self.deck)
            player.calculate_points()