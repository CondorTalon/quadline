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
        self.player1 = Player.Player(self, "Y")
        self.player2 = Player.Player(self, "R")
        self.current_player = self.player1

    def get_current_player(self) -> Player:
        """
        Returns the player that can make a move at the time this function is called

        Parameters:
        :return:
        """
        return self.current_player

    def get_other_player(self, player: Player) -> Player:
        if player == self.player1:
            return self.player2
        return self.player1

    def is_game_over(self) -> bool:
        """
        Returns whether or not the game is over.

        Parameters:
        :return:
        """
        if self.current_player is None or not self.grid.available_moves():
            return True
        return False

    def get_winner(self, column):
        if self.is_game_over():
            return self.grid.get_token(self.grid.depth(column), column)

    def make_move(self, column: int) -> bool:
        """
        Makes a move for the current player at the specified column.

        Parameters:
        :int column: the column the move wil be made in
        :return: True if the move is successfully made. False otherwise.
        """
        if self.grid.drop_token(column, self.get_current_player().get_color()):
            self.current_player = self.get_other_player(self.current_player)
            if self.grid.is_quadline(column):
                # print("QUADLINE")
                self.current_player = None
            return True
        return False

