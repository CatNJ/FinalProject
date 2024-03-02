from pygame import *
from classes.GameSprite import GameSprite


class Player(GameSprite):
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
