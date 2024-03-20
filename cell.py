from point import Point
from line import Line
from graphics import Window

class Cell:
    def __init__(self, x1, y1, x2, y2, win = None, has_left_Wall = True
                 , has_right_Wall = True, has_top_Wall = True
                 , has_bottom_Wall = True ) -> None:
        self.__x1 = x1  # top left x
        self.__x2 = x2  # bottom right x
        self.__y1 = y1  # top left y
        self.__y2 = y2  # bottom right y
        self.__win = win
        self.has_left_Wall = has_left_Wall
        self.has_right_Wall = has_right_Wall
        self.has_top_Wall = has_top_Wall
        self.has_bottom_Wall = has_bottom_Wall
        self.visited = False

    def draw(self):
        if self.__win is None:
            return
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)
        self.__draw_wall(top_left, bottom_left, self.has_left_Wall)
        self.__draw_wall(top_right, bottom_right, self.has_right_Wall)
        self.__draw_wall(top_left, top_right, self.has_top_Wall)
        self.__draw_wall(bottom_left, bottom_right, self.has_bottom_Wall)

    def __draw_wall(self, p1, p2, has_wall):
        color = "black" if has_wall else "white"
        self.__win.draw_line(Line(p1, p2), color)

    def draw_move(self, to_cell, undo = False):
        if self.__win is None:
            return
        color = "grey" if undo else "red"
        start_point = Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2 )
        end_point = Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2 )
        self.__win.draw_line(Line(start_point, end_point), color)
