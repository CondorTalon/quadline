from typing import List


class QuadlineGrid:
    """
    Class QuadlineGrid represents a grid which a game of Quadline is played on
    and has methods that updates the state of the grid as players in a game
    interacts with it using methods in class Quadline.

    Attributes:
    :int row: a integer representing a row in a Quadline Grid.
    :int col: a integer representing a column in a Quadline Grid.
        Each space in the grid can be located through a row and a col
        coordinate.
    :List[List] grid: the nested list representation of a Quadline grid
    """
    row: int
    col: int
    grid: List[List[str]]

    def __init__(self) -> None:
        """
        The constructor of the class, instantiates a new grid
        """
        self.row = 6
        self.col = 7
        self.grid = []

        for y in range(self.row):
            temp_row = []
            for x in range(self.col):
                temp_row.append(" ")
            self.grid.append(temp_row)

    def grid_string(self) -> None:
        """
        Prints the Quadline grid
        """
        for i in range(6):
            print(self.grid[i])
        print("-----------------------------------")

    def check_bounds(self, row: int, col: int) -> bool:
        """
        Check a specified row and column on grid to see if that is in the grid.
        location.

        Parameters:
        :param row: The row of the location being checked
        :param col: The column of the location being checked
        :return: True if the location specified is in the grid. False otherwise.
        """
        return 0 <= row < self.row and 0 <= col < self.col

    def valid_column(self, col: int) -> bool:
        """
        Checks if there is space in the column specified that new tokens can
        occupy.

        Parameters:
        :param col: The column being checked
        :return: True if there is space for a token. False otherwise.
        """

        return self.check_bounds(0, col) and self.grid[0][col] == " "

    def depth(self, col) -> int:
        """
        Returns the lowest unoccupied space in the specified column

        Parameters:
        :param col: int (0 to 7)
        :return: an int representing the lowest unoccupied space in specified
        col
        """
        row = 0
        while self.get_token(row, col) == " ":
            row += 1
        return row

    def drop_token(self, col: int, token: str) -> bool:
        """
        Adds player token to first unoccupied row, starting from the bottom of
        the grid, in the specified column and returns the result of the move.

        Parameters:
        :param col: The column the token will drop into.
        :param token: The string representation of a token.
        :return: True if dropped token results in win, False otherwise
        """
        col = int(col)
        if self.valid_column(col):
            self.grid[self.depth(col)-1][col] = token
            return True
        return False

    def get_token(self, row: int, col: int) -> str:
        """
        Check a specified row and column on grid to see if there exist a token
        in that location.

        Parameters:
        :param row: The row of the location being checked
        :param col: The column of the location being checked
        :return: True if there is a token on the location. False otherwise.
        """
        if self.check_bounds(row, col):
            return self.grid[row][col]

    def check_quadline(self, row: int, col: int, drow: int, dcol: int) -> bool:
        """
        Given the location and direction, checks to see if that specified
        direction results in a Quadline.

        Parameters:
        :param row: int (0 to 6)
        :param col: int (0 to 7)
        :param drow: int (-1 to 1)
        :param dcol: int (-1 to 1)
        :return: True if specified location and direction results in win, False
        otherwise
        """
        count = 1
        token = self.get_token(row, col)
        count_token = 1
        while self.check_bounds(row+drow, col+dcol) and count <= 3:
            if self.grid[row+drow][col+dcol] == token:
                row += drow
                col += dcol
                count_token += 1
            if count_token == 4:
                return True
            count += 1
        return False

    def is_quadline(self, col: int) -> bool:
        """
        Checks if a Quadline has been formed on the grid.

        Parameters:
        :return: True if the tokens that successfully formed a Quadline, False
        otherwise.
        """
        row = self.depth(col)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and self.check_quadline(row, col,
                                                                   i, j):
                    return True
        return False

    def available_moves(self) -> bool:
        """
        Checks if the grid still has moves

        Parameters:
        :return: True if grid has moves, False otherwise
        """
        has_move = False
        for i in range(self.col):
            if self.valid_column(i):
                has_move = True
        return has_move
