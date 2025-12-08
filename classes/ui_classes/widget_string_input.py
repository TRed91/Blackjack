from tkinter import *
from tkinter import ttk

class StringInputWidget:

    def __init__(self, root : Tk, prompt : str, title : str = "Enter name"):
        
        self.value = ""

        root.title(title)

        # setup main frame
        self.mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # setup labels
        ttk.Label(self.mainframe, text=prompt).grid(column=2, row=1, sticky=(W, E))

            # info message label
        self.message = StringVar()
        ttk.Label(self.mainframe, textvariable=self.message).grid(column=2, row=4, sticky=(W, E))

        # setup number entry
        self.player_name = StringVar()
        input_field = ttk.Entry(self.mainframe, width=7, textvariable=self.player_name)
        input_field.grid(column=2, row=2, sticky=(W, E))

        # setup enter button
        ttk.Button(self.mainframe, text="Enter", command=self.set_value).grid(column=2, row=3, sticky=(W, E))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        input_field.focus()
        root.bind("<Return>", self.set_value)

    def set_value(self, *args) -> None:
        input = self.player_name.get()
        if input.isspace() or len(input) == 0:
            self.message.set("Input can't be empty or whitespace only")
        else:
            self.value = input
            self.mainframe.quit()
    
    def get_value(self, *args) -> str:
        return self.value