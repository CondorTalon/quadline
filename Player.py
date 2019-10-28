from typing import Dict, List

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
        
    def get_color() -> str:
        """
        Returns the color of the player
        """
        return self.color
    def has_move() -> bool:
        """
        Returns whether the player has a move on the grid
        """
        raise NotImplementedError
    
        
    
    
    
        
    
