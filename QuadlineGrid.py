from typing import List


class QuadlineGrid:
    """
    Class QuadlineGrid represents a grid which a game of Quadline is played on
    and has methods that updates the state of the grid as players in a game interacts
    with it using methods in class Quadline.

    Attributes:
    :int row: a integer representing a row in a Quadline Grid.
    :int col: a integer representing a column in a Quadline Grid.
        Each space in the grid can be located through a row and a col coordinate.
    :List[List] grid: the nested list representation of a Quadline grid
    """
    row: int
    col: int
    grid: List[List[str]]

    def __init__(self, row: int, column: int) -> None:
        """
        The constructor of the class, instantiates a newgrid
        """
        self.row = 6
        self.col = 7
        #TODO: Flexible implementation of row and col
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
        :str token: The string representation of a token.
        :return: None
        """
        if self.valid_column(col):
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
        if check_counds(row, col):
            return (not self.grid[row][col] == " ")
        else:
            return False

    def valid_column(self, col: int) -> bool:
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

    def check_bounds(self, row: int, col: int) -> bool:
        """
        Check a specified row and column on grid to see if that is in the grid.
        location.
        
        Parameters:
        :int row: The row of the location being checked
        :int col: The column of the location being checked
        :return: True if the location specified is in the grid. False otherwise.
        """
        return 0 <= row < self.row and 0 <= col < self.col

    def check_quadline(self) -> Optional[str]:
        """
        Checks if a Quadline has been formed on the grid. If a Quadline is formed,
        returns the token it is made out of.

        Parameters:
        :return: The tokens that successfully formed a Quadline, or None if no Quadline is
        found on the grid.
        """
        for r in range(self.row):
            for c in range(self.column):
                if has_token(r, c):
                    token = self.[r][c]
                    for drow in range(-1, 2):
                        for dcol in range(-1, 2):
                            count = 1
                            while check_bounds(r + count * drow, c + count * dcol):
                                if self.grid[r + count * drow][c + count * dcol] == token:
                                    count += 1
                                else:
                                    break
                            if token >= 3:
                                return token
        return None
                    
