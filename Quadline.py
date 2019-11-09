from quadline import QuadlineGrid, Player

class Quadline:
    """
    The Quadline Class represents an instance of a Quadline game and has methods that is used to
    operate the game.

    Attributes:
    grid: the quadline grid the game will use
    player1 and player2: the two players playing the game
    current_player: the player that can make the next move
    """
    grid: QuadlineGrid
    player1: Player
    player2: Player
    current_player: str

    def __init__(self):
        """
        Instantiates the class Quadline
        """
        self.grid = QuadlineGrid.QuadlineGrid()
        self.player1 = Player.Player(self.grid, "Yellow")
        self.player2 = Player.Player("Red")
        self.current_player = 'P1'

    def get_current_player(self) -> str:
        return self.current_player

    def is_game_over(self) -> bool:
        """
        Returns whether or not the game is over.
        """
        if (not self.player1.has_move) or (not self.player2.has_move):
            return True
        else:
            return False

    def make_move(self, column: int) -> bool:
        """
        Makes a move for the current player. If the move is invalid, the player is prompted to try again.
        If the move is valid, places a token in the specified column and passes the turn to the other player.
        Returns whether the move was successfully made.
        """
        valid_move = self.grid.valid_location(column)
        if valid_move and not self.is_game_over():
            if self.current_player == 'P1':
                self.grid.drop_token(column, self.player1.color)
                self.current_player = 'P2'
            else:
                self.grid.drop_token(column, self.player2.color)
                self.current_player = 'P1'
            return True
        else:
            return False

