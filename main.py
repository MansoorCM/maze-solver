from graphics import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    p1, p2 = Point(1, 1), Point(300, 400)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()