from config import pr, SCREEN_WIDTH, SCREEN_HEIGHT


class Grid():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.row_len = self.rows - 1
        self.columns_len = self.columns - 1
        self.grid_cells = [[0] * self.columns for _ in range(self.rows)]
    
    def set_new_grid_pos(self, x, y, value, new_grid):
        self.value = value
        new_grid.grid_cells[x][y] = self.value