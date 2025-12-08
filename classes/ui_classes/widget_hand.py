from tkinter import *
from tkinter import ttk
from classes.card import Card

class HandWidget:

    def __init__(self, parent : Frame, row : int):

        self.cardframe = ttk.Frame(parent, padding=(5, 3, 5, 3))
        self.cardframe.grid(column=2, row = row, sticky=(N, W, E, S))

        #self.cardframe.configure(width=70*6+10, height=110)
        
        for child in self.cardframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def set_cards(self, cards : list[Card]):
        for i in range(len(cards)):
            path = f"static/{cards[i].number.value}_{cards[i].type.value}.png"
            img = PhotoImage(file=path)
            label = ttk.Label(self.cardframe, image=img)
            label.grid(column= i + 1, row=1, sticky=W)
            label.image = img
            