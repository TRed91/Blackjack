from classes.game import Game
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else "console"
game = Game(mode)

if mode == "gui":
    root = game.get_root()

    def start():
        game.run()
        root.quit()

    root.after(0, start)
    root.mainloop()
else:
    game.run()