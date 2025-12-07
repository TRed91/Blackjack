from classes.io_interface import IO_Interface, Player
from classes.results import *

class ConsoleIO(IO_Interface):
    def __init__(self):
        pass    
    


    def get_number_input(self, start: int, end: int, prompt : str) -> int:
        while True:
            print(prompt)
            print(f"Enter a number from {start} to {end}")
            input_str : str = str(input())

            if input_str.isdigit():
                num_input = int(input_str)
                if num_input >= start and num_input <= end:
                    return num_input
            
            print(f"Input must be a valid number between {start} and {end}")



    def get_string_input(self, prompt: str) -> str:
        while True:
            print(prompt)
            input_str : str = str(input())

            if len(input_str) == 0:
                print("Input can't be empty!")
            elif input_str.isspace():
                print("Input can't be whitespace!")
            else:
                return input_str
    


    def print_info_msg(self, msg : str) -> None:
        print(f"\n-->\t{msg}\n")



    def print_block_msg(self, messages : list[str]) -> None:
        print("\n==========")
        for msg in messages:
            print(msg)
        print("==========\n")



    def print_hand(self, player : Player, is_first_round : bool = False) -> None:
        # Print header
        print(f"\n======= {player.name}'s hand:")

        # Format card printing 
        numbers_line = ""
        types_line = ""

            # hide second card if is dealer and first round
        if (is_first_round and not player.is_human):
            numbers_line = f"| {player.hand[0].number.value} |\t|###|"
            types_line = f"| {player.hand[0].type.value} |\t|###|"
        else:
            for card in player.hand:
                numbers_line += f"| {card.number.value} |\t"
                types_line += f"| {card.type.value} |\t"

        # Print cards
        print("*****\t" * len(player.hand))
        print(numbers_line)
        print(types_line)
        print(("*****\t" * len(player.hand)) + "\n")
        
        # Print points or blackjack
        if player.has_blackjack():
            print("\tBLACKJACK!")
        else:
            print(f"\tTotal points: {player.points}")
        print()
    


    def print_board(self, players : list[Player], dealer : Player, is_first_round : bool) -> None:
        
        self.print_hand(dealer, is_first_round)

        for player in players:
            self.print_hand(player)
    


    def print_result(self, players : list[Player], dealer : Player) -> None:
        print("\n======= Game Result =======")

        self.print_board(players, dealer, False)

        max_points = float("-inf")
        winner : Player = None

        if dealer.result != PlayerResult.BUST:
            max_points = dealer.points
            winner = dealer

        messages = [ f"{dealer.name} - {dealer.result.value}: {dealer.points}" ]

        for player in players:
            messages.append(f"{player.name} - {player.result.value}: {player.points}")
            if player.result != PlayerResult.BUST:
                if player.points > max_points:
                    max_points = player.points
                    winner = player

        self.print_block_msg(messages)

        if winner:
            self.print_info_msg(f"{winner.name} WINS THE ROUND!")
        else:
            self.print_info_msg(f"DRAW!")