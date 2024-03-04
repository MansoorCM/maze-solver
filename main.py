from graphics import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    # draw sample line
    p1, p2 = Point(1, 1), Point(300, 400)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    
    # draw sample cell
    cell = Cell(100, 100, 300, 400, win)
    cell.draw()
    cell2 = Cell(350, 100, 550, 400, win)
    cell2.draw()
    cell.draw_move(cell2, True)
    win.wait_for_close()

main()