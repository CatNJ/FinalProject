import math
import json
import random
from data.GameSprite import GameSprite

class Enemy(GameSprite):
    def __init__(self, window, image, x, y, width, height, target, health, speed, damage):
        super().__init__(window, image, x, y, width, height)
        self.target = target
        self.health = health
        self.speed = speed
        self.damage = damage

    def move(self):
        try:
            dx, dy = (self.target.rect.x - self.rect.x,
                      self.target.rect.y - self.rect.y)
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            self.rotate(self.target.get_pos())
        except ZeroDivisionError:
            pass

    def collide_player(self):
        if self.rect.colliderect(self.target.rect):
            return True
        return False

    def update(self):
        self.move()
        self.draw()

class Spawner:
    def __init__(self, window, waves, starting_points, increment_rate, player):
        self.window = window
        self.waves = waves
        self.wave = 1
        self.points = starting_points
        self.increment_rate = increment_rate
        self.player = player
        self.enemys = []
        self.WIN_WIDTH, self.WIN_HEIGHT = window.get_size()
        
        with open("data/zombies.json", "r", encoding="utf-8") as file:
            self.zombies_list = json.load(file)

    def start(self):
        if len(self.enemys) == 0:
            while self.points > 0:
                zombie = random.choice(list(self.zombies_list.keys()))
                price = self.zombies_list[zombie]["price"]

                if self.points >= price:
                    enemy = Enemy(self.window, "sprites/zombie/" + self.zombies_list[zombie]["skin"],
                                 random.randint(-self.WIN_WIDTH-self.WIN_WIDTH/2, self.WIN_WIDTH+self.WIN_WIDTH/2),
                                 random.randint(-self.WIN_WIDTH-self.WIN_WIDTH/2, self.WIN_HEIGHT+self.WIN_HEIGHT/2),
                                 28*2.5, 21*2.5,
                                 self.player,
                                 self.zombies_list[zombie]["health"],
                                 self.zombies_list[zombie]["speed"],
                                 self.zombies_list[zombie]["damage"])
                    self.enemys.append(enemy)
                    self.points -= price

            self.points = self.increment_rate * self.wave
            self.wave += 1
