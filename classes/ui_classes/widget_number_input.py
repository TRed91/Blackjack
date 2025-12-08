from tkinter import *
from tkinter import ttk
from classes.ui_classes.gui_io import GuiIO

class NumPlayersWidget:

    def __init__(self, io : GuiIO, range_start : int, range_end : int, prompt : str, title : str = "Number input"):
        
        self.range_start = range_start
        self.range_end = range_end
        self.return_num = -1

        io.root.title(title)

        # setup main frame
        self.mainframe = ttk.Frame(io.root, padding=(3, 3, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # setup labels
        ttk.Label(self.mainframe, text=prompt).grid(column=2, row=1, sticky=(W, E))

            # info message label
        self.message = StringVar()
        ttk.Label(self.mainframe, textvariable=self.message).grid(column=2, row=4, sticky=(W, E))

        # setup number entry
        self.num_players = StringVar()
        num_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.num_players)
        num_entry.grid(column=2, row=2, sticky=(W, E))

        # setup enter button
        ttk.Button(self.mainframe, text="Enter", command=self.set_num).grid(column=2, row=3, sticky=(W, E))

        io.root.columnconfigure(0, weight=1)
        io.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        num_entry.focus()
        io.root.bind("<Return>", self.set_num)

    def set_num(self, *args) -> None:
        value = self.num_players.get()
        if value.isdigit():
            num = int(value)
            if num >= self.range_start and num <= self.range_end:
                self.return_num = num
                self.mainframe.quit()
            else:
                self.message.set(f"Input must be between {self.range_start} and {self.range_end}")
        else:
            self.message.set("Input must be a number")
    
    def get_num(self, *args) -> int:
        return self.return_num