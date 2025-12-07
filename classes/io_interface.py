from abc import ABC, abstractmethod
from classes.player import Player

class IO_Interface(ABC):
    @abstractmethod
    def get_number_input(self, start: int, end: int, prompt: str) -> int:
        pass

    @abstractmethod
    def get_string_input(self, prompt: str) -> str:
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