from pygame import *
from random import randint

WIN_WIDTH, WIN_HEIGHT = 900, 600
FPS = 60

class Game():
    def __init__(self):
        init()
        font.init()
        mixer.init()

        self.window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        display.set_caption("Zombie Killer")

    def loop(self):
        pass

    def start(self):
        clock = time.Clock()
        run = True

        while run:
            for e in event.get():
                if e.type == QUIT:
                    run = False

            self.loop()

            display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()

    

