from classes.io_interface import IO_Interface
from classes.consoleio import ConsoleIO

class IO_Factory:
    def get_console_io() -> IO_Interface :
        return ConsoleIO()