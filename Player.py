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
        Returns the color of token assigned to the player

        Parameters:
        :returns:
        Colour of the token as a string
        """
        return self.color

    def get_move(self):

        """
        Gets the input for the column from the user, ensures that the value is in the parameters, and
        returns the value 

        Parameters:
        :return: The integer value inputted by the user
        """
        bad_input = True
        input_column = None

        while bad_input:
            input_column = input("Enter column 0 - 6")
            if input_column.__len__() == 1 and str(input_column) in "0123456":
                bad_input = False
        return int(input_column)

    def has_move(self) -> bool:
        """
        Returns whether the player has made a move on the grid
        
        Parameters: 
        :return: _____
        """
        raise NotImplementedError







