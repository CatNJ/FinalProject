from pygame import *
from classes.GameSprite import GameSprite
from random import randint
import math

class Player(GameSprite):
    def __init__(self, window, image, x, y, width, height):
        super().__init__(window, image, x, y, width, height)
        self.player_speed = 5
        self.bullets = sprite.Group()
        self.bullet_delay = 300
        self.last_shoot = time.get_ticks()
        self.camera_sprites = []

    def set_camera_sprites(self, sprites):
        self.camera_sprites = sprites

    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a]:
            self.rect.x -= self.player_speed
            for sprite in self.camera_sprites:
                sprite.rect.x += self.player_speed
        elif key_pressed[K_d]:
            self.rect.x += self.player_speed
            for sprite in self.camera_sprites:
                sprite.rect.x -= self.player_speed
        if key_pressed[K_w]:
            self.rect.y -= self.player_speed
            for sprite in self.camera_sprites:
                sprite.rect.y += self.player_speed
        elif key_pressed[K_s]:
            self.rect.y += self.player_speed
            for sprite in self.camera_sprites:
                sprite.rect.y -= self.player_speed

    def shoot(self):
        current_time = time.get_ticks()
        if mouse.get_pressed()[0] and current_time - self.last_shoot > self.bullet_delay:
            mouse_x, mouse_y = mouse.get_pos()
            self.bullets.add(PlayerBullet(self.window, "sprites/bullet.png", 
                                          self.rect.x+(self.image.get_width()/2), self.rect.y+(self.image.get_height()/2),
                                          10, 10,
                                          mouse_x, mouse_y,))
            self.last_shoot = current_time

        self.bullets.update()

    def bullet_collide(self, enemys):
        for enemy in enemys:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.health -= 50
                    self.bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemys.remove(enemy)

                
    def update(self):
        self.move()
        self.draw()
        self.rotate(mouse.get_pos())
        self.shoot()

class PlayerBullet(GameSprite):
    def __init__(self, window, image, x, y, width, height, mouse_x, mouse_y):
        super().__init__(window, image, x, y, width, height)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = randint(30, 35)
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        self.draw()
