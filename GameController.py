from quadline import Player, Quadline

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

    def __init__(self) -> None:
        """
        The constructor of the class, instantiates the controller
        """
        self.game = Quadline.Quadline()
        self.play()

    def play(self):
        """
        Begin the game which the two players play, with both players take turn making moves,
        and return the winner once the game is finished.

        :return: The player who won the game being played. 
        """
        move = None
        self.game.grid.get_grid()
        while not self.game.is_game_over():
            move = self.game.get_current_player().get_move()
            self.game.make_move(move)
            self.game.grid.get_grid()
        print(self.game.get_winner(move), " wins!")


if __name__ == "__main__":
    GameController()
