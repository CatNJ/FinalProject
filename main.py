from pygame import *
from random import randint
from classes.Player import Player

WIN_WIDTH, WIN_HEIGHT = 900, 600
FPS = 60

class Game():
    def __init__(self):
        init()
        font.init()
        mixer.init()

        self.window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        display.set_caption("Zombie Killer")

        self.clock = time.Clock()
        self.run = True

        self.player = Player(self.window, "sprites/player/player_pistol.png",
                             WIN_WIDTH/2, WIN_HEIGHT/2,
                             28*2, 21*2)

    def loop(self):
        self.player.move()
        self.player.draw()
        self.player.rotate(mouse.get_pos())
        self.player.shoot()

    def start(self):
        while self.run:
            self.window.fill((0, 0, 0))

            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            self.loop()

            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()

    

