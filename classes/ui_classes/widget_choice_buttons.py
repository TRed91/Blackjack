from tkinter import *
from tkinter import ttk
from classes.player_choice import PlayerChoice

class ChoiceButtonWidget:

    def __init__(self, parent : Frame, row : int):

        self.row = row
        self.choice = PlayerChoice.NONE
        self.pressed_signal = IntVar(master=parent)
        
        self.buttonsframe = ttk.Frame(parent, padding=(5,3,5,3))
        self.buttonsframe.grid(column=4, row=row, sticky=E)

        self.take_btn = ttk.Button(self.buttonsframe, text="Take", command=self.take_pressed)
        self.take_btn.grid(column=1, row=1, sticky=(W, E), padx=5, pady=5)
        self.take_btn.config(state=DISABLED)

        self.stand_btn = ttk.Button(self.buttonsframe, text="Stand", command=self.stand_pressed)
        self.stand_btn.grid(column=2, row=1, sticky=(W, E), padx=5, pady=5)
        self.stand_btn.config(state=DISABLED)



    def enable_buttons(self) -> None:
        self.take_btn.config(state=NORMAL)
        self.stand_btn.config(state=NORMAL)



    def disable_buttons(self) -> None:
        self.take_btn.config(state=DISABLED)
        self.stand_btn.config(state=DISABLED)



    def take_pressed(self, *args) -> None:
        self.choice = PlayerChoice.HIT
        self.pressed_signal.set(1)
        self.disable_buttons()



    def stand_pressed(self, *args) -> None:
        self.choice = PlayerChoice.STAND
        self.pressed_signal.set(2)
        self.disable_buttons()



    def get_choice(self) -> PlayerChoice:
        current_choice = self.choice
        self.choice = PlayerChoice.NONE
        return current_choice
