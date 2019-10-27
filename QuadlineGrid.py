from typing import List


class QuadlineGrid:
    """
    Constructs the Quadline grid and updates the grid as needed when players
    play their moves.
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

     def drop_token(self, length, width, token):
        
        #adds a token to the row and column chosen by player(s)
        self.grid[length][width] = token

    def valid_location(self, col) -> bool:
        
        #checks if the token can be dropped in player's choice of column 
        return self.grid[0][col] == " "    
