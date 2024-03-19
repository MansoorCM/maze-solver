from graphics import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    screen_x, screen_y = 800, 600
    margin = 50
    num_rows, num_cols = 16, 12
    cell_size_x = ( screen_x - 2 * margin ) // num_rows
    cell_size_y = ( screen_y - 2 * margin ) // num_cols
    win = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()
    
main()