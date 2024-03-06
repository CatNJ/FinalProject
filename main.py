from pygame import *
from pygame.transform import *
from pygame.image import load
from random import randint
from classes.Player import Player
from classes.Enemy import Enemy

WIN_WIDTH, WIN_HEIGHT = 900, 900
FPS = 60

class Game():
    def __init__(self):
        init()
        font.init()
        mixer.init()

        mouse.set_visible(False)

        self.window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        display.set_caption("Zombie Killer")

        self.clock = time.Clock()
        self.run = True

        self.bg = scale(load("sprites/grass.png").convert(), (WIN_WIDTH, WIN_HEIGHT))
        self.cursor_image = scale(load("sprites/cursor.png"), (64, 64))
        self.player = Player(self.window, "sprites/player/player_pistol.png",
                             WIN_WIDTH/2, WIN_HEIGHT/2,
                             28*2.5, 21*2.5)
        self.zombie = Enemy(self.window, "sprites/zombie/zombie_default.png",
                             0, 0,
                             28*2.5, 21*2.5,
                             self.player)
        
        
    def draw_cursor(self):
        mouse_x, mouse_y = mouse.get_pos()
        image_width, image_height = self.cursor_image.get_size()
        self.window.blit(self.cursor_image, (mouse_x-(image_width/2), mouse_y-(image_height/2)))

    def loop(self):
        self.player.move()
        self.player.draw()
        self.player.rotate(mouse.get_pos())
        self.player.shoot()

        self.zombie.move()
        self.zombie.draw()

        self.draw_cursor()

    def start(self):
        while self.run:
            self.window.blit(self.bg, (0, 0))

            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            self.loop()

            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()

    

