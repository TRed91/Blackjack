from tkinter import *
from tkinter import ttk
from classes.card import Card

class HandWidget:

    def __init__(self, parent : Frame, row : int):

        self.cardframe = ttk.Frame(parent, padding=(5, 3, 5, 3))
        self.cardframe.grid(column=2, row = row, sticky=(N, W, E, S))
        
        for child in self.cardframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def set_cards(self, cards : list[Card]):
        for i in range(len(cards)):
            path = f"static/{cards[i].number.value}_{cards[i].type.value}.png"
            img = PhotoImage(file=path)
            label = ttk.Label(self.cardframe, image=img)
            label.grid(column= i + 1, row=1, sticky=W)
            label.image = img

    def set_dealer_cards(self, cards: list[Card]):
        card_path = f"static/{cards[0].number.value}_{cards[0].type.value}.png"
        hidden_path = "static/bg.png"
        card_img = PhotoImage(file=card_path)
        bg_img = PhotoImage(file=hidden_path)

        label_card = ttk.Label(self.cardframe, image=card_img)
        label_card.grid(column=1, row=1, sticky=W)
        label_card.image = card_img

        hidden_card = ttk.Label(self.cardframe, image=bg_img)
        hidden_card.grid(column=2, row=1, sticky=W)
        hidden_card.image = bg_img