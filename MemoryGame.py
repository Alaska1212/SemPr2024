import tkinter as tk
from GameBoard import GameBoard

class MemoryGame:
    LEVELS = {
        1: (2, 2),
        2: (2, 3),
        3: (3, 4),
    }

    def __init__(self, root):
        self.root = root
        self.level = 1
        self.message_label = tk.Label(
            self.root, text='', font=('Helvetica', 16)
        )
        self.message_label.grid(row=4, columnspan=4)
        self.start_game()

    def start_game(self):
        self.board = GameBoard(
            self.root,
            *self.LEVELS[self.level],
            self.next_level,
        )

    def next_level(self):
        self.message_label.config(text='Вітаємо! Ви відкрили всі зображення!')
        self.level += 1
        if self.level > 3:
            self.level = 1
        self.root.after(2000, self.restart_game)

    def restart_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.message_label = tk.Label(
            self.root, text='', font=('Helvetica', 16)
        )
        self.message_label.grid(row=4, columnspan=4)
        self.start_game()