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
        :return: the game grid in nested list format
        """
        return self.grid

    def drop_token(self, col: int, token: str) -> None:
        """
        Adds player token to next unoccupied row of the grid in the specified
        col
        :param col: int from 0-6
        :param token: str 'P1' or 'P2'
        :return: None
        """
        y = 0
        while y < 6 and self.has_token(y, col):
            y += 1
        self.grid[y-1][col] = token

    def has_token(self, row: int, col: int) -> bool:
        """
        Check row and col on grid to see if there is a token in that location
        :param row: int from 0-5
        :param col: int from 0-6
        :return: bool depending on if there is a token in specified location
        """
        return self.grid[row][col] == " "

    def valid_location(self, col: int) -> bool:
        """
        checks if the token can be dropped in player's choice of column
        """
        return self.grid[0][col] == " "
