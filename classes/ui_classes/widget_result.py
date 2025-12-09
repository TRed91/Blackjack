from tkinter import *
from tkinter import ttk
from classes.player import Player, PlayerResult

class ResultWidget:

    def __init__(self, root : Tk, players : list[Player], dealer : Player):
        
        self.top = Toplevel(root)
        self.top.title("Game Result")
        self.top.transient(root)
        self.top.grab_set()

        self.frame = ttk.Frame(self.top, padding=(10,10,10,10))
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))


        ttk.Label(self.frame, text="Game Results").grid(column=2, row=1, sticky=W)

        max_points = dealer.points if dealer.result != PlayerResult.BUST else float('-inf')
        winner : Player = dealer if dealer.result != PlayerResult.BUST else None

        blackjack_count = 0

        # Set Dealer Result
        self.draw_result(dealer, 2)

        if dealer.has_blackjack():
            blackjack_count += 1
            winner = dealer

        # Set Player Results
        for i in range(len(players)):

            self.draw_result(players[i], i + 3)

            if players[i].result != PlayerResult.BUST and players[i].points > max_points:
                max_points = players[i].points
                winner = players[i]

            if players[i].has_blackjack():
                blackjack_count += 1
                winner = players[i]


        # if multiple players have blackjack it's a draw
        if blackjack_count > 1:
            winner = None
        
        winner_msg = f"{winner.name} WON!" if winner != None else "DRAW!"

        ttk.Label(self.frame, text=winner_msg).grid(column=2, row=len(players) + 3)

        ttk.Button(self.frame, text="Quit", command=self.quit_pressed).grid(column=3, row=len(players) + 4)



    def quit_pressed(self, *args) -> None:
        self.top.destroy()



    def draw_result(self, player : Player, row : int) -> None:
        result_text = "" if player.has_blackjack() or player.result == PlayerResult.NONE else player.result.value
        points_text = "BLACKJACK!" if player.has_blackjack() else player.points
        ttk.Label(self.frame, text=f"{player.name}:").grid(column=1, row=row, sticky=W)
        ttk.Label(self.frame, text=result_text).grid(column=2, row=row, sticky=W)
        ttk.Label(self.frame, text=points_text).grid(column=3, row=row, sticky=W)