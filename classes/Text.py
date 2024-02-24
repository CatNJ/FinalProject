from pygame import *
from classes.GameSprite import GameSprite

class Text(sprite.Sprite):
    def __init__(self, window, text, x, y, font_size=22, font_name="Impact", color=(255,255,255)):
        self.window = window
        self.font = font.SysFont(font_name, font_size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        
    def draw(self):
        self.window.blit(self.image, self.rect)
    
    def set_text(self, new_text):
        self.image = self.font.render(new_text, True, self.color)