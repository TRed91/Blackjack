from tkinter import *
from tkinter import ttk

class StringInputWidget:

    def __init__(self, root : Tk, prompt : str, title : str = "Enter name"):
        
        self.value = ""
        self.done = BooleanVar(master=root, value=False)

        self.top = Toplevel(root)
        self.top.title(title)
        self.top.transient(root)
        self.top.grab_set()

        # setup main frame
        self.mainframe = ttk.Frame(self.top, padding=(3, 3, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # setup labels
        ttk.Label(self.mainframe, text=prompt).grid(column=2, row=1, sticky=(W, E))

            # info message label
        self.message = StringVar(master=self.top)
        ttk.Label(self.mainframe, textvariable=self.message).grid(column=2, row=4, sticky=(W, E))

        # setup number entry
        self.player_name = StringVar(master=self.top)
        input_field = ttk.Entry(self.mainframe, width=7, textvariable=self.player_name)
        input_field.grid(column=2, row=2, sticky=(W, E))

        # setup enter button
        ttk.Button(self.mainframe, text="Enter", command=self.set_value).grid(column=2, row=3, sticky=(W, E))

        self.top.columnconfigure(0, weight=1)
        self.top.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.top.focus_set()
        input_field.focus_set()
        self.top.bind("<Return>", self.set_value)

    def set_value(self, *args) -> None:
        input = self.player_name.get()
        if input.isspace() or len(input) == 0:
            self.message.set("Input can't be empty or whitespace only")
        else:
            self.value = input
            self.done.set(True)
            #self.mainframe.quit()
            self.top.grab_release()
            self.top.destroy()
    
    def get_value(self, *args) -> str:
        return self.value