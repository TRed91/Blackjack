# Blackjack
Boot.dev personal project

This app allows you to play a round of blackjack.

To run this game make sure you go python3 installed.

To play in cli mode type `./main.sh console` into your cli.
To play in gui mode type `./main.sh gui` into your cli.

The gui was implemented using tkinter.

I created an IO_Interface like so:
```
class IO_Interface(ABC):
    @abstractmethod
    def get_number_input(self, start: int, end: int, prompt: str) -> int:
        pass

    @abstractmethod
    def get_string_input(self, prompt: str) -> str:
        pass

    @abstractmethod
    def get_player_choice(self, player : Player) -> PlayerChoice:
        pass

    @abstractmethod
    def print_info_msg(self, msg : str) -> None:
        pass

    @abstractmethod
    def print_block_msg(self, messages : list[str]) -> None:
        pass

    @abstractmethod
    def print_hand(self, player : Player, is_first_round : bool) -> None:
        pass

    @abstractmethod
    def print_board(self, players : list[Player], dealer : Player, is_first_round : bool) -> None:
        pass

    @abstractmethod
    def print_result(self, players : list[Player], dealer : Player) -> None:
        pass
```

Console_IO and Gui_IO both implement the interface.
The Gui_IO class also acts as a wrapper for the tkinter implementation.

With this object oriented approach i can leverage polymorphism and have
my game loop only interact with the IO_Interface.

depending on the argument passed to main the IO_Factory inject the appropriate interface.
```
class IO_Factory:

    def get_io(mode : str) -> IO_Interface :
        if (mode.lower() == "gui"):
            return GuiIO()
        if (mode.lower() == "console"):
            return ConsoleIO()
        raise Exception("Invalid run argument. Needs to be either be 'console' or 'gui'.")
```

The mode however does default to 'console' if no arguments are passed.