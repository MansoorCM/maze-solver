from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cell()

    def create_cell(self):
        self._cells = []
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                x1, y1 = self.x1 + i * self.cell_size_x, self.y1 + j * self.cell_size_y
                x2, y2 = x1 + self.cell_size_x, y1 + self.cell_size_y
                self._cells[-1].append(Cell(x1, y1, x2, y2, self.win))

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.draw_cell(r, c)

    def draw_cell(self, i, j):
        self._cells[i][j].draw()
        self.animate()

    def break_entrance_and_exit(self):
        self._cells[0][0].has_top_Wall = False
        self.draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_Wall = False 
        self.draw_cell(self.num_rows - 1, self.num_cols - 1)

    def break_wall_r(self, i, j):
        self._cells[i][j].visited = True
        nextCells = []
        self.add_cell(nextCells, i - 1, j)
        self.add_cell(nextCells, i + 1, j)
        self.add_cell(nextCells, i, j - 1)
        self.add_cell(nextCells, i, j + 1)
        
        while nextCells:
            idx = random.randint(0, len(nextCells) - 1)
            nextCells[idx], nextCells[-1] = nextCells[-1], nextCells[idx]
            r, c = nextCells.pop()
            if not self._cells[r][c].visited:
                self.break_wall_between_two_adjacent_cells(i, j, r, c)
                self.break_wall_r(r, c)

        self.draw_cell(i, j)

    def add_cell(self, cells, i, j):
        if i >= 0 and i < self.num_rows and j >= 0 and j < self.num_cols and not self._cells[i][j].visited:
            cells.append([i, j])

    def break_wall_between_two_adjacent_cells(self, i, j, r, c):    # moving from (i, j) to (r, c)
        if i + 1 == r:  # down
            self._cells[i][j].has_bottom_Wall = False
            self._cells[r][c].has_top_Wall = False
        elif i == r + 1: # up
            self._cells[i][j].has_top_Wall = False
            self._cells[r][c].has_bottom_Wall = False
        elif j == c + 1: # left
            self._cells[i][j].has_left_Wall = False
            self._cells[r][c].has_right_Wall = False
        else:   # right
            self._cells[i][j].has_right_Wall = False
            self._cells[r][c].has_left_Wall = False

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02)
