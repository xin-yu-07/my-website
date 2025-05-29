# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:13:46 2025

@author: Avator
"""

import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root, size=4):
        self.root = root
        self.size = size
        self.buttons = []
        self.flipped = []
        self.values = list(range(1, (size * size) // 2 + 1)) * 2
        random.shuffle(self.values)
        self.create_board()

    def create_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(self.root, text=" ", width=6, height=3,
                                command=lambda i=i, j=j: self.flip(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def flip(self, i, j):
        idx = i * self.size + j
        btn = self.buttons[i][j]
        if btn["text"] == " " and len(self.flipped) < 2:
            btn["text"] = str(self.values[idx])
            self.flipped.append((i, j))
            if len(self.flipped) == 2:
                self.root.after(700, self.check_match)

    def check_match(self):
        (i1, j1), (i2, j2) = self.flipped
        v1 = self.values[i1 * self.size + j1]
        v2 = self.values[i2 * self.size + j2]
        if v1 != v2:
            self.buttons[i1][j1]["text"] = " "
            self.buttons[i2][j2]["text"] = " "
        self.flipped = []
        self.check_win()

    def check_win(self):
        if all(btn["text"] != " " for row in self.buttons for btn in row):
            messagebox.showinfo("Congratulations", "You matched all the cards!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Memory Match Game")
    game = MemoryGame(root, size=4)  # 你可以改成 size=6 來玩 6x6
    root.mainloop()
