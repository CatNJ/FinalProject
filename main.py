from pygame import *
from pygame.transform import *
from pygame.image import load
from data.GameSprite import GameSprite
from data.Player import Player
from data.Enemy import Spawner
from data.Text import Text

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
        
        self.text_fps = Text(self.window, "",
                             10, 10, 32)
        self.text_health = Text(self.window, "",
                           10, 42, 32)
        self.text_wave = Text(self.window, "",
                              10, 74, 32)
        self.text_enemies_left = Text(self.window, "",
                                      10, 106, 32)
        self.text_game_over = Text(self.window, "Game Over!",
                                   WIN_WIDTH/2-len("Game Over!")*(75/4), WIN_HEIGHT/2-75, 75,
                                   color=(255, 0, 0))

        self.all_sprites = [self.bg]
        self.spawner = Spawner(self.window, 10, 10, 5, self.player)

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

    def draw_ui(self):
        self.text_fps.set_text(f"FPS: {round(self.clock.get_fps(), 1)}")
        self.text_health.set_text(f"Health: {self.player.health}")
        self.text_wave.set_text(f"Wave: {self.spawner.wave}")
        self.text_enemies_left.set_text(f"Enemies left: {len(self.spawner.enemys)}")

        self.text_fps.draw()
        self.text_health.draw()
        self.text_wave.draw()
        self.text_enemies_left.draw()

    def loop(self):
        self.player.update()
        self.player.bullet_collide(self.spawner.enemys)
        self.spawner.start()

        for zombie in self.spawner.enemys:
            zombie.update()
            if zombie.collide_player():
                self.player.health -= zombie.damage
                self.spawner.enemys.remove(zombie)

        self.player.set_camera_sprites(self.all_sprites, self.spawner.enemys)
        self.draw_cursor()

    def start(self):
        while self.run:
            for e in event.get():
                if e.type == QUIT:
                    self.run = False

            self.draw_bg()
            
            if self.player.health > 1:
                self.loop()

            else:
                self.text_game_over.draw()

            self.draw_ui()

            display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.start()

    

