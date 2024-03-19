import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self) -> None:
        num_rows = 16
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows) 
        self.assertEqual(len(maze._cells[0]), num_cols)

    def test_break_entrance_and_exit(self):
        num_rows = 16
        num_cols = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze.break_entrance_and_exit()
        self.assertEqual(maze._cells[0][0].has_top_Wall, False) 
        self.assertEqual(maze._cells[-1][-1].has_bottom_Wall, False) 

if __name__ == "__main__":
    unittest.main()