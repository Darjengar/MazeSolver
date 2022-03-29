#!/usr/bin/env python
# Author : Darjengar 03/25/2022, License: GPL 3.0
# written in Python 3.9

import tkinter as tk
import GridMap
import time

WIN_WIDTH = 800
WIN_HEIGHT = 800
BLOCK_SIZE = 64

class MazeSolverGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maze_matrix = [
                [1,1,1,2],
                [0,1,0,1],
                [0,1,0,1],
                [3,1,1,1]
            ]
        self.title("Maze Solver")
        self.geometry("{0}x{1}".format(len(self.maze_matrix) * BLOCK_SIZE, len(self.maze_matrix) * BLOCK_SIZE))
        self.resizable(width=False, height=False)
        self.option_add("*tearOff", tk.FALSE)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.sketch = GridMap.GridMap(self, len(self.maze_matrix) * BLOCK_SIZE, len(self.maze_matrix) * BLOCK_SIZE)
        self.sketch.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.draw_maze()
        self.after(1000, self.solve_maze)

    def solve_maze(self):
        if self.solve(0, len(self.maze_matrix)-1):
            print("Lösbar")
        else:
            print("Nicht lösbar")
        self.draw_maze()

    def draw_maze(self):
        for iii in range(0, len(self.maze_matrix)):
            for jjj in range(0, len(self.maze_matrix)):
                if self.maze_matrix[iii][jjj] == 0:
                    self.sketch.fill_block_helper(jjj, iii, "gray")
                elif self.maze_matrix[iii][jjj] == 1:
                    self.sketch.fill_block_helper(jjj, iii, "white")
                elif self.maze_matrix[iii][jjj] == 2:
                    self.sketch.fill_block_helper(jjj, iii, "green")
                elif self.maze_matrix[iii][jjj] == 3:
                    self.sketch.fill_block_helper(jjj, iii, "blue")

    def clear_maze(self):
        for iii in range(0, WIN_HEIGHT // 64):
            for jjj in range(0, WIN_WIDTH // 64):
                self.maze_matrix[jjj][iii] = 0
                self.sketch.clear_block(jjj, iii)

    def solve(self, row, col):
        if self.maze_matrix[row][col] == 3:
            self.maze_matrix[row][col] = 2
            return True
        self.maze_matrix[row][col] = 2
        # Check bottom border
        if row+1 > len(self.maze_matrix)-1:
            # Dead end
            if self.maze_matrix[row][col-1] == 0:
                self.maze_matrix[row][col] = 1
            else:
                # Step left
                if self.maze_matrix[row][col-1] == 1 or self.maze_matrix[row][col-1] == 3:
                    if self.solve(row, col-1):
                        return True
                    self.maze_matrix[row][col] = 1
        elif col-1 < 0:
            # Dead end
            if self.maze_matrix[row+1][col] == 0:
                self.maze_matrix[row][col] = 1
            else:
                # Step down
                if self.maze_matrix[row+1][col] == 1 or self.maze_matrix[row+1][col] == 3:
                    if self.solve(row+1, col):
                        return True
                    self.maze_matrix[row][col] = 1
        else:
            # Dead end
            if self.maze_matrix[row+1][col] == 0 and self.maze_matrix[row][col-1] == 0:
                if row != 0 or col != len(self.maze_matrix)-1:
                    self.maze_matrix[row][col] = 1
            else:
                # Step left
                if self.maze_matrix[row][col-1] == 1 or self.maze_matrix[row][col-1] == 3:
                    if self.solve(row, col-1):
                        return True
                # Step down
                if self.maze_matrix[row+1][col] == 1 or self.maze_matrix[row+1][col] == 3:
                    if self.solve(row+1, col):
                        return True
                if row != 0 or col != len(self.maze_matrix)-1:
                    self.maze_matrix[row][col] = 1
        return False



if __name__ == '__main__':
    app = MazeSolverGUI()
    app.mainloop()