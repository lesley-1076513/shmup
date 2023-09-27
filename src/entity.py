import pygame as pg
import random

class Entity():
    def __init__(self, col, pos, size, lives, atk_speed):
        self.colour = col
        self.position = pos
        self.size = size
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.lives = lives
        self.atk_delay = False
        self.atk_speed = atk_speed
        self.atk_timer = 0
    def attack(self):
        attack_sfx = pg.mixer.Sound(f"sfx/shoot{random.randint(1,6)}.wav")
        attack_sfx.play()
    def update(self, clock):
        if self.atk_delay:
                self.atk_timer += clock.get_rawtime()
                if self.atk_timer >= self.atk_speed:
                    self.atk_delay = False
                    self.atk_timer = 0
    def draw(self):
         pass
