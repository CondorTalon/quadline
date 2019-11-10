from typing import List


class QuadlineGrid:
    """
    Class QuadlineGrid represents the grid which a game of Quadline is played on
    and has methods that updates the state of the grid as players make moves.

    Attributes:
    row and col: col stands for 'column'. Each space in the grid can be located
        through a row and a col coordinate.
    grid: the nested list representation of the actual grid
    """
    row: int
    col: int
    grid: List[List[str]]

    def __init__(self) -> None:
        """
        The constructor of the class, instantiates a new game grid
        """
        self.row = 6
        self.col = 7
        self.grid = []

        for y in range(self.row):
            temp_row = []
            # creates a temporary row until there are six rows
            for x in range(self.col):
                temp_row.append(" ")
                # creates the columns for each row
            self.grid.append(temp_row)
            # constructs the actual game grid by appending the individual rows
            # to the main list

    def get_grid(self) -> List[List[str]]:
        """
        Returns the Quadline grid

        Parameters:
        :return: the game grid in nested list format
        """
        return self.grid

    def drop_token(self, col: int, token: str) -> None:
        """
        Adds player token to first unoccupied row, starting from the bottom of the grid,
        in the specified column.
        
        Parameters:
        :int col: The column the token will drop into.
        :str token: The string representation of a token. Can be 'P1' or 'P2'.
        :return: None
        """
        if self.valid_location(col):
            y = 0
            while self.has_token(y, col):
                y += 1
            self.grid[y][col] = token

    def has_token(self, row: int, col: int) -> bool:
        """
        Check a specified row and column on grid to see if there exist a token in that
        location.
        
        Parameters:
        :int row: The row of the location being checked
        :int col: The column of the location being checked
        :return: True if there is a token on the location. False otherwise.
        """
        return (not self.grid[row][col] == " ")

    def valid_location(self, col: int) -> bool:
        """
        Checks if there is space in the column specified that new tokens can occupy.

        Parameters:
        :int col: The column being checked
        :return: True if there is space for a token. False otherwise.
        """
        for r in range(self.row):
            if not self.has_token(r, col):
                return True
        return False
