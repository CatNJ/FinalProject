import math
from pygame import sprite
from pygame.transform import *
from pygame.image import load
from pygame import math as pmath


class GameSprite(sprite.Sprite):
    def __init__(self, window, image, x, y, width, height):
        super().__init__()
        self.window = window

        self.image = scale(load(image).convert_alpha(), (width, height))
        self.base_image = self.image
        self.width = width
        self.height = height

        self.hitbox_rect = self.base_image.get_rect(center = pmath.Vector2(x, y))
        self.rect = self.hitbox_rect.copy()

    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def rotate(self, pos):
        self.x_change_pos_sprite = (pos[0] - self.rect.centerx)
        self.y_change_pos_sprite = (pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_pos_sprite, self.x_change_pos_sprite))
        self.image = rotate(self.base_image, -self.angle)

    def move_camera(self, direction, speed):
        if direction[0] == "-":
            self.rect.x -= speed

        elif direction[0] == "+":
            self.rect.x += speed

        if direction[1] == "-":
            self.rect.y -= speed

        elif direction[1] == "+":
            self.rect.y += speed

    
    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))