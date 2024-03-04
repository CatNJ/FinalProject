from pygame import *
from classes.GameSprite import GameSprite
import math

class Player(GameSprite):
    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a]:
            self.rect.x -= 5
        elif key_pressed[K_d]:
            self.rect.x += 5
        if key_pressed[K_w]:
            self.rect.y -= 5
        elif key_pressed[K_s]:
            self.rect.y += 5


class PlayerBullet:
    def __init__(self, window, x, y, mouse_x, mouse_y, damage=50):
        self.window = window
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 30
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.damage = damage

    def shoot(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        draw.circle(self.window, (255,255,0), (self.x, self.y), 5)