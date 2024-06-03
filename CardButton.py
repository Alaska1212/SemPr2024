import tkinter as tk


class CardButton(tk.Button):
    def __init__(self, master, image, hidden_image, *args, **kwargs):
        super().__init__(master, image=hidden_image, *args, **kwargs)
        self.hidden_image = hidden_image
        self.image = image
        self.is_flipped = False

    def flip(self):
        if not self.is_flipped:
            self.config(image=self.image)
            self.is_flipped = True
        else:
            self.config(image=self.hidden_image)
            self.is_flipped = False