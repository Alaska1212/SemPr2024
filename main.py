import tkinter as tk
from MemoryGame import MemoryGame


if __name__ == '__main__':
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
