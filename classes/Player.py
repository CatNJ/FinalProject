from pygame import *
from classes.GameSprite import GameSprite
from random import randint
import math

class Player(GameSprite):
    def __init__(self, window, image, x, y, width, height):
        super().__init__(window, image, x, y, width, height)
        self.bullets = []
        self.bullet_delay = 300
        self.last_shoot = time.get_ticks()

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

    def shoot(self):
        current_time = time.get_ticks()
        if mouse.get_pressed()[0] and current_time - self.last_shoot > self.bullet_delay:
            mouse_x, mouse_y = mouse.get_pos()
            self.bullets.append(PlayerBullet(self.window, self.rect.x+(self.image.get_width()/2), self.rect.y+(self.image.get_height()/2), mouse_x, mouse_y))
            self.last_shoot = current_time

        for bullet in self.bullets:
            bullet.shoot()
                

class PlayerBullet:
    def __init__(self, window, x, y, mouse_x, mouse_y, damage=50):
        self.window = window
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = randint(30, 35)
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.damage = damage

    def shoot(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        draw.circle(self.window, (255,255,0), (self.x, self.y), 5)