from random import randint
from pygame import *
from pygame.transform import *
from pygame.image import load
from random import randint
from data.GameSprite import GameSprite
from data.Player import Player
from data.Enemy import Enemy

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

        self.bg = GameSprite(self.window, "sprites/grass.png", 0, 0, WIN_WIDTH*2, WIN_HEIGHT*2)
        self.cursor_image = scale(load("sprites/cursor.png"), (64, 64))
        self.player = Player(self.window, "sprites/player/player_pistol.png",
                             WIN_WIDTH/2, WIN_HEIGHT/2,
                             28*2.5, 21*2.5)

        self.zombies = []
        self.all_sprites = [self.bg]
        
        for _ in range(10):
            self.zombie = Enemy(self.window, "sprites/zombie/zombie_default.png",
                                 randint(-WIN_WIDTH-WIN_WIDTH/2, WIN_WIDTH+WIN_WIDTH/2), randint(-WIN_WIDTH-WIN_WIDTH/2, WIN_HEIGHT+WIN_HEIGHT/2),
                                 28*2.5, 21*2.5,
                                 self.player,
                                 100, 2)
            self.zombies.append(self.zombie)

        self.player.set_camera_sprites(self.all_sprites, self.zombies)


    def draw_cursor(self):
        mouse_x, mouse_y = mouse.get_pos()
        image_width, image_height = self.cursor_image.get_size()
        self.window.blit(self.cursor_image, (mouse_x-(image_width/2), mouse_y-(image_height/2)))

    def draw_bg(self):
        self.bg.draw()
        self.bg.draw(-WIN_WIDTH*2, -WIN_HEIGHT*2)
        self.bg.draw(WIN_WIDTH*2, -WIN_HEIGHT*2)
        self.bg.draw(-WIN_WIDTH*2, 0)
        self.bg.draw(0, -WIN_HEIGHT*2)

        self.bg.draw(WIN_WIDTH*2, WIN_HEIGHT*2)
        self.bg.draw(-WIN_WIDTH*2, WIN_HEIGHT*2)
        self.bg.draw(0, -WIN_HEIGHT*2)
        self.bg.draw(WIN_WIDTH*2, 0)
        self.bg.draw(0, WIN_HEIGHT*2)

    def loop(self):
        self.player.update()
        self.player.bullet_collide(self.zombies)
        for zombie in self.zombies:
            zombie.update()

        self.draw_cursor()

    def start(self):
        while self.run:
            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            self.draw_bg()
            self.loop()

            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()

    

