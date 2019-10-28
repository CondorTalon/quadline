
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
    
    def __init__(grid: QuadlineGrid):
        """
        Instantiates the class Quadline
        """
        self.grid = grid
        self.player1 = player1
        self.player2 = player2
        self.current_player = 'P1'
        
    def get_current_player() -> str:
        return self.current_player

    def is_game_over() -> bool:
        """
        Returns whether or not the game is over.
        """
        if (not player1.has_move) or (not player2.has_move):
            return true
        else return false

    def make_move(column) -> bool:
        """
        Makes a move for the current player. If the move is invalid, the player is prompted to try again.
        If the move is valid, places a token in the specified column and passes the turn to the other player.
        Returns whether the move was successfully made.
        """
        valid_move = grid.valid_location(self, col)
        if valid_move and not is_game_over:
            if self.current_player == 'P1':
                grid.drop_token(self, column, player1.color)
                self.current_player = 'P2'
                return true
            else
                grid.drop_token(self, column, player2.color)
                self.current_player = 'P1'
                return true
        else return false

