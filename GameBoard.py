import random
from CardButton import CardButton

from PIL import Image, ImageTk

class GameBoard:
    def __init__(self, root, rows, cols, flip_callback):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.flip_callback = flip_callback

        # Завантаження зображень
        self.images = [
                          ImageTk.PhotoImage(Image.open(img).resize((200, 200)))
                          for img in [f'./images/енот{i + 1}.jpg' for i in range(7)]
                      ][: (rows * cols) // 2]
        hidden_image = ImageTk.PhotoImage(
            Image.open('./images/back.jpg').resize((200, 200))
        )

        # Дублювання зображень та їх випадкове розташування
        self.images *= 2
        random.shuffle(self.images)

        self.buttons = []
        self.flipped = []

        for i in range(rows):
            row = []
            for j in range(cols):
                image = self.images.pop()
                button = CardButton(
                    self.root,
                    image,
                    hidden_image,
                    command=lambda i=i, j=j: self.flip_card(i, j),
                )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def flip_card(self, i, j):
        button = self.buttons[i][j]
        if len(self.flipped) < 2 and not button.is_flipped:
            button.flip()
            self.flipped.append((i, j))
            if len(self.flipped) == 2:
                self.root.after(1000, self.check)

    def check(self):
        i1, j1 = self.flipped[0]
        i2, j2 = self.flipped[1]
        button1 = self.buttons[i1][j1]
        button2 = self.buttons[i2][j2]
        if button1.image == button2.image:
            button1.config(state='disabled')
            button2.config(state='disabled')
        else:
            button1.flip()
            button2.flip()
        self.flipped.clear()
        if all(
                button['state'] == 'disabled'
                for row in self.buttons
                for button in row
        ):
            self.flip_callback()