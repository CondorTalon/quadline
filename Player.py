from quadline import Quadline


class Player:
    """
    Class Player represents a single player in a Quadline game.

    Attributes:
    :Quadline game: the game Quadline that player will play on
    :str color: the token color of the player
    """
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
        :returns: Colour of the token as a string
        """
        return self.color
