from typing import Dict, List

"""
class Controller executes the game Quadline between two players.
Attributes:
game: the game Quadline that player will play on
color: the token color of the player
"""
class GameController:
    player1: Player
    player2: Player
    game: Quadline
    
    def __init__(self, game: Quadline, player1: Player, player2: Player) -> None:
        """
        The constructor of the class, intantiates the controller
        """
        self.game = game
        self.player1 = player1
        self.player2 = player2
        
    def play() -> str:
        """
        Returns the winner of the game once the game is fininshed and makes the
        player play each other
        """
        raise NotImplementedError
    
    if __name__ == "__main__":
        play()
    
        
    
    
    
        
    