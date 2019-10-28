from typing import Dict, List

"""
Class Controller executes the game Quadline between two players.

Attributes:
player1 and player2: the two players playing the game
game: the game of Quadline that player will play on
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
        Begin the game which the two players play, with both players take turn making moves,
        and return the winner once the game is finished.
        """
        while not game.is_game_over:
            if game.current_player == player1:
                player1.get_move()
            if game.current_player == player2:
                player2.get_move()
        winner = game.get_winner()
        if winner == player1 or winner == player2:
            return winner.__str__ + " won the Game!"
        else:
            return "The match ended in a draw."
                
    
    if __name__ == "__main__":
        play()
    
        
    
    
    
        
    
