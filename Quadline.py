from quadline import QuadlineGrid, Player

class Quadline:
    """
    Class Quadline represents an instance of a Quadline game and has methods that is used
    to operate the game and update te grid it is played on.

    Attributes:
    :QuadlineGrid grid: the Quadline grid this game will use
    :Player player1, player2: the two players playing the game
    :Player current_player: the player that can make the next move
    """
    grid: QuadlineGrid
    player1: Player
    player2: Player
    current_player: Player

    def __init__(self):
        """
        The constructor of the class, instantiates a new game
        """
        self.grid = QuadlineGrid.QuadlineGrid()
        self.player1 = Player.Player(self, "Yellow")
        self.player2 = Player.Player(self, "Red")
        self.current_player = self.player1

    def get_current_player(self) -> Player:
        """
        Returns the player that can make a move at the time this function is called

        Parameters:
        :return:
        """
        return self.current_player

    def is_game_over(self) -> bool:
        """
        Returns whether or not the game is over.

        Parameters:
        :return:
        """
        if self.check_quadline() == None:
            if (not self.player1.has_move) or (not self.player2.has_move):
                return True
            else:
                return False
        else:
            return True

    def check_quadline(self) -> Optional[Player]:
        """
        Checks if a Quadline has been formed on the grid. If a Quadline is formed,
        checks which player formed it.

        Parameters:
        :return: The player who successfully formed a Quadline, or None if no Quadline is
        found on the grid.
        """
        someone_might_win = self.grid.check_quadline()
        if someone_might_win == None:
            return None
        elif someone_might_win == self.get_player_token(self.player1):
            return self.player1
        else:
            return self.player2

    def get_player_token(self, player: Player) -> str:
        """
        Return the token used by the specified player.

        Parameters:
        :return:
        """
        return player.get_color()
        

    def make_move(self, column: int) -> bool:
        """
        Makes a move for the current player at the specified column.

        Parameters:
        :int column: the column the move wil be made in
        :return: True if the move is successfully made. False otherwise.
        """
        valid_move = self.grid.valid_column(column)
        if valid_move and not self.is_game_over():
            if self.current_player == self.player1:
                self.grid.drop_token(column, self.player1.color)
                self.current_player = self.player2
            else:
                self.grid.drop_token(column, self.player2.color)
                self.current_player = self.player1
            return True
        else:
            return False

