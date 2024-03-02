from pygame import *
from pygame.transform import *
from pygame.image import load


class GameSprite(sprite.Sprite):
    def __init__(self, window, image, x, y, width, height):
        super().__init__()
        self.window = window

        self.image = scale(load(image).convert_alpha(), (width, height))
        self.width = width
        self.height = height

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))