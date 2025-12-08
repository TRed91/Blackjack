from classes.io_interface import IO_Interface
from classes.consoleio import ConsoleIO
from classes.ui_classes.gui_io import GuiIO

class IO_Factory:

    def get_io(mode : str) -> IO_Interface :
        if (mode.lower() == "gui"):
            return GuiIO()
        if (mode.lower() == "console"):
            return ConsoleIO()
        raise Exception("Invalid run argument. Needs to be either 'console' or 'gui'.")