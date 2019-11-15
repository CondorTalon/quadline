from typing import Dict, List
from quadline import Quadline

"""
Class Player represents a single player in a Quadline game.

Attributes:
game: the game Quadline that player will play on
color: the token color of the player
"""


class Player:
    game: Quadline
    color: str

    def __init__(self, game: Quadline, color: str) -> None:
        """
        The constructor of the class, intantiates a player
        """
        self.game = game
        self.color = color

    def get_color(self) -> str:
        """
        Returns the color of the player
        """
        return self.color

    def get_move(self):
        bad_input = True
        input_column = None

        while bad_input:
            input_column = input("Enter column 0 - 6")
            if input_column.__len__() == 1 and str(input_column) in "0123456":
                bad_input = False
        return int(input_column)

    def has_move(self) -> bool:
        """
        Returns whether the player has a move on the grid
        """
        raise NotImplementedError







