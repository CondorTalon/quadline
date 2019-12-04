from quadline import QuadlineGrid, Player


class Quadline:
    """
    Class Quadline represents an instance of a Quadline game and has methods
    that is used to operate the game and update te grid it is played on.

    Attributes:
    :QuadlineGrid grid: the Quadline grid this game will use
    :Player player1, player2: the two players playing the game
    :Player current_player: the player that can make the next move
    """
    grid: QuadlineGrid
    player1: Player
    player2: Player
    current_player: Player
    last_move: int

    def __init__(self) -> None:
        """
        The constructor of the class, instantiates a new game
        """
        self.grid = QuadlineGrid.QuadlineGrid()
        self.player1 = Player.Player(self, "Y")
        self.player2 = Player.Player(self, "R")
        self.current_player = self.player1
        self.last_move = None

    def get_current_player(self) -> Player:
        """
        Returns the player that can make a move at the time this function is
        called

        Parameters:
        :return: The current player's turn
        """
        return self.current_player

    def get_other_player(self, player: Player) -> Player:
        """
        Returns the opposite of the specified player

        Parameters:
        :param player: player1 or player2
        :return: the opposite player
        """
        if player == self.player1:
            return self.player2
        return self.player1

    def is_game_over(self) -> bool:
        """
        Returns whether or not the game is over.

        Parameters:
        :return: true if the game is over, false otherwise
        """
        if self.current_player is None or not self.grid.available_moves():
            return True
        return False

    def get_winner(self) -> str:
        """
        Returns the string color of the player who won

        Parameters:
        :return: the string Y or R depending on the winner
        """
        column = self.get_last_move()
        if self.is_game_over() and self.current_player is None:
            return self.grid.get_token(self.grid.depth(column), column)

    def get_last_move(self) -> int:
        """
        Returns the column of the last move played

        Parameters:
        :return: an int of the last move played
        """
        return self.last_move

    def make_move(self, column: int) -> bool:
        """
        Makes a move for the current player at the specified column.

        Parameters:
        :param column: the column the move wil be made in
        :return: True if the move is successfully made. False otherwise.
        """
        if self.current_player is not None and \
                self.grid.drop_token(column,
                                     self.get_current_player().get_color()):
            self.current_player = self.get_other_player(self.current_player)
            if self.grid.is_quadline(column):
                self.current_player = None
            self.last_move = column
            return True
        return False
