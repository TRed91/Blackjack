class ConsoleIO:
    def __init__(self):
        pass    
    
    def get_number_input(self, start: int, end: int) -> int:
        while True:
            print(f"Enter a number from {start} to {end}")
            input_str : str = str(input())

            if input_str.isdigit():
                num_input = int(input_str)
                if num_input >= start and num_input <= end:
                    return num_input
            
            print(f"Input must be a valid number between {start} and {end}")

    def get_string_input(self, prompt: str, input_type : str = "Input") -> str:
        while True:
            print(prompt)
            input_str : str = str(input())

            if len(input_str) == 0:
                print(f"{input_type} can't be empty!")
            elif input_str.isspace():
                print(f"{input_type} can't be whitespace!")
            else:
                return input_str
    