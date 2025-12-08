from classes.io_interface import *
from classes.ui_classes.gameboard import GameBoard
from tkinter import *

class GuiIO(IO_Interface):

    def __init__(self):
        self.root = Tk()
        
        #self.__set_window()

        self.gameboard = GameBoard(self.root)

    def get_number_input(self, start: int, end: int, prompt: str = None) -> int:
        from classes.ui_classes.widget_number_input import NumPlayersWidget
        widget_num_players = NumPlayersWidget(self.root, start, end, prompt, "Enter number of players")
        self.root.mainloop()
        return widget_num_players.get_num()



    def get_string_input(self, prompt: str) -> str:
        from classes.ui_classes.widget_string_input import StringInputWidget
        widget = StringInputWidget(self.root, prompt, "Player Name Input")
        self.root.mainloop()
        return widget.get_value()


    def get_player_choice(self, player : Player) -> PlayerChoice:
        return self.gameboard.get_choice(player)


    def print_info_msg(self, msg : str) -> None:
        self.gameboard.set_message_label(msg)



    def print_block_msg(self, messages : list[str]) -> None:
        pass



    def print_hand(self, player : Player, is_first_round : bool = False) -> None:
        self.gameboard.update_hand(player)



    def print_board(self, players : list[Player], dealer : Player, is_first_round : bool = False) -> None:
        self.gameboard = GameBoard(self.root)
        self.gameboard.set_dealer_hand(dealer)
        for i in range(len(players)):
            self.gameboard.insert_player(players[i], i + 1)
        self.root.mainloop()



    def print_result(self, players : list[Player], dealer : Player) -> None:
        pass



    def __set_window(self) -> None:
        WIDTH = 800
        HEIGHT = 650

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        pos_x = 100
        pos_y = 150

        self.root.geometry(f"{WIDTH}x{HEIGHT}+{pos_x}+{pos_y}")