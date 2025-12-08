from classes.io_interface import IO_Interface
from classes.player import *
from tkinter import *

class GuiIO(IO_Interface):

    def __init__(self):
        self.root = Tk()

    def get_number_input(self, start: int, end: int, prompt: str = None) -> int:
        from classes.ui_classes.widget_number_input import NumPlayersWidget
        widget_num_players = NumPlayersWidget(self, start, end, prompt, "Enter number of players")
        self.root.mainloop()
        return widget_num_players.get_num()



    def get_string_input(self, prompt: str) -> str:
        from classes.ui_classes.widget_string_input import StringInputWidget
        widget = StringInputWidget(self.root, prompt, "Player Name Input")
        self.root.mainloop()
        return widget.get_value()



    def print_info_msg(self, msg : str) -> None:
        pass



    def print_block_msg(self, messages : list[str]) -> None:
        pass



    def print_hand(self, player : Player, is_first_round : bool) -> None:
        pass



    def print_board(self, players : list[Player], dealer : Player, is_first_round : bool) -> None:
        pass



    def print_result(self, players : list[Player], dealer : Player) -> None:
        pass