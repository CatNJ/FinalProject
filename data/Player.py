from pygame import *
from data.GameSprite import GameSprite
from random import randint
import math

class Player(GameSprite):
    def __init__(self, window, image, x, y, width, height):
        super().__init__(window, image, x, y, width, height)
        self.x = x
        self.y = y
        self.health = 100
        self.player_speed = 5
        self.bullets = sprite.Group()
        self.bullet_delay = 300
        self.last_shoot = time.get_ticks()
        self.camera_sprites = []

    def set_camera_sprites(self, sprites, zombies):
        self.camera_sprites = sprites
        self.zombies_camera = zombies

    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_a]:
            if self.x + self.player_speed > -900:
                self.x -= self.player_speed
                for sprite in self.camera_sprites:
                    sprite.rect.x += self.player_speed
                for sprite in self.zombies_camera:
                    sprite.rect.x += self.player_speed

        elif key_pressed[K_d]:
            if self.x + self.player_speed < 900:
                self.x += self.player_speed
                for sprite in self.camera_sprites:
                    sprite.rect.x -= self.player_speed
                for sprite in self.zombies_camera:
                    sprite.rect.x -= self.player_speed

        if key_pressed[K_w]:
            if self.y + self.player_speed > -900:
                self.y -= self.player_speed
                for sprite in self.camera_sprites:
                    sprite.rect.y += self.player_speed
                for sprite in self.zombies_camera:
                    sprite.rect.y += self.player_speed

        elif key_pressed[K_s]:
            if self.y + self.player_speed < 900:
                self.y += self.player_speed
                for sprite in self.camera_sprites:
                    sprite.rect.y -= self.player_speed
                for sprite in self.zombies_camera:
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
                        try:
                            enemys.remove(enemy)
                        except ValueError:
                            pass

                
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
        if (self.rect.x > self.window.get_width() or self.rect.x < 0 or
            self.rect.y > self.window.get_height() or self.rect.y < 0):
            self.kill()

        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        self.draw()
