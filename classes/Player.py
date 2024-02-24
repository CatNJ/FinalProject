from pygame import *
from classes.GameSprite import GameSprite

class Player(GameSprite):
    def __init__(self, window, x, y, width, height, color):
        super().__init__(window, x, y, width, height, color)
        self.width = width
        self.height = height
        self.color = color
        self.rect = Rect(x, y, width, height)

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
            self.rect.x -= 5
        elif keys_pressed[K_d]:
            self.rect.x += 5
        if keys_pressed[K_w]:
            self.rect.y -= 5
        elif keys_pressed[K_s]:
            self.rect.y += 5
