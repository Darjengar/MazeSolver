#!/usr/bin/env python
# Author : Darjengar 03/25/2022, License: GPL 3.0
# written in Python 3.9

from textwrap import fill
import tkinter as tk
from tkinter import ttk
from turtle import color

BLOCK_SIZE = 64

class GridMap(tk.Canvas):
    def __init__(self, parent, width, height, *args, **kwargs):
        super().__init__(parent,background="white", *args, **kwargs)
        self.width = width
        self.height = height
        self.draw_grid(width // BLOCK_SIZE, height // BLOCK_SIZE, BLOCK_SIZE+1)
        self.idmap = [[0 for x in range(0, width // BLOCK_SIZE)] for y in range(0, height // BLOCK_SIZE)]

    def draw_grid(self, width, height, blocksize):
        color = "black"
        # horizontal
        for iii in range(0, height+1):
            self.create_line(1, iii * blocksize + 1, blocksize * width + 2, iii * blocksize + 1, fill=color)
        # vertical
        for iii in range(0, width+1):
            self.create_line(iii * blocksize + 1, 1, iii * blocksize + 1, blocksize * height + 1, fill=color)

    def fill_block(self, xpos, ypos, blocksize, color):
        self.idmap[ypos][xpos] = self.create_rectangle(xpos * blocksize + 1, ypos * blocksize + 1, xpos * blocksize + blocksize + 1, ypos * blocksize + blocksize + 1, fill=color, outline="black")

    def fill_block_helper(self, xpos, ypos, color):
        self.fill_block(xpos, ypos, BLOCK_SIZE+1, color)

    def clear_block(self, xpos, ypos):
        self.delete(self.idmap[ypos][xpos])
        self.idmap[ypos][xpos] = 0

    def clear_screen(self):
        for iii in range(0, self.width // 64):
            for jjj in range(0, self.height // 64):
                self.clear_block(jjj, iii)