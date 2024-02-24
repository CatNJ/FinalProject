from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, window, x, y, width, height, color):
        super().__init__()
        self.window = window
        self.rect = Rect(x, y, width, height)
        self.rect.x = x
        self.rect.y = y
        self.color = color

    def draw(self):
        draw.rect(self.window, self.color, self.rect)