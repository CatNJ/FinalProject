import math
import pygame
from classes.GameSprite import GameSprite

class Enemy(GameSprite):
    def __init__(self, window, image, x, y, width, height, target):
        super().__init__(window, image, x, y, width, height)
        self.target = target
        self.speed = 2

    def move(self):
        try:
            dx, dy = (self.target.rect.x - self.rect.x,
                      self.target.rect.y - self.rect.y)
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            self.rotate(self.target.get_pos())
        except ZeroDivisionError:
            pass

    def update(self):
        self.move()
        self.draw()

