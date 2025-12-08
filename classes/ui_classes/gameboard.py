from tkinter import *
from tkinter import ttk
from classes.player import Player
from classes.ui_classes.widget_hand import Card, HandWidget
from classes.ui_classes.widget_choice_buttons import ChoiceButtonWidget, PlayerChoice

class GameBoard:

    def __init__(self, root : Tk):

        self.root = root
        self.players : dict[str, tuple[HandWidget, ChoiceButtonWidget, Label]] = {}
        
        root.title("Gameboard")

        # setup main frame
        self.mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # setup labels
        ttk.Label(self.mainframe, text="Dealer's Hand:").grid(column=1, row=1, sticky=W)

        self.message = StringVar()
        ttk.Label(self.mainframe, textvariable=self.message).grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.mainframe, text="Points", justify="center").grid(column=3, row=2, sticky=(W,  E))



        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



    def set_message_label(self, msg : str):
        self.message.set(msg)



    def set_dealer_hand(self, dealer: Player):
        HandWidget(self.mainframe, 1).set_cards(dealer.hand)



    def insert_player(self, player : Player, row : int) -> None:
        ttk.Label(self.mainframe, text=f"{player.name}'s Hand:", justify="right").grid(column=1, row=row + 2, sticky=W)
        
        hw = HandWidget(self.mainframe, row + 2)
        hw.set_cards(player.hand)
        
        points_label = ttk.Label(self.mainframe, text=player.points, justify="center")
        points_label.grid(column=3, row=row + 2, sticky=(W, E))
        
        bw = ChoiceButtonWidget(self.mainframe, row + 2)
        bw.disable_buttons()

        self.players[player.name] = (hw, bw, points_label)


    def get_choice(self, player : Player) -> PlayerChoice:
        btns = self.players[player.name][1]
        
        btns.enable_buttons()
        self.root.wait_variable(btns.pressed_signal)
        choice = btns.get_choice()
        if choice != PlayerChoice.NONE:
            return choice
        


    def update_hand(self, player : Player):
        self.players[player.name][0].set_cards(player.hand)
        self.players[player.name][2].config(text=player.points)