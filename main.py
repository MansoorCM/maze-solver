from graphics import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    screen_x, screen_y = 800, 600   # x is horizontal, y is vertical.
    margin = 50
    num_rows, num_cols = 12, 16
    cell_size_x = ( screen_x - 2 * margin ) // num_cols
    cell_size_y = ( screen_y - 2 * margin ) // num_rows
    win = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.break_entrance_and_exit()
    maze.break_wall_r(0, 0)
    print('maze created.')
    maze.reset_cells_visited()
    if maze.solve():
        print('maze solved.')
    else:
        print('maze cannot be solved.')
    win.wait_for_close()
    
main()