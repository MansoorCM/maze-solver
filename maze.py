from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None) -> None:
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

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02)
