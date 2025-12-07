from classes.game import Game
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else "console"
game = Game(mode)
game.run()