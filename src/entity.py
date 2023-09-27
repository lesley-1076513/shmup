import pygame as pg
import random
import projectile

class Entity():
    def __init__(self, col, pos, size, lives, atk_speed):
        self.colour = col
        self.position = pos
        self.size = size
        self.speed = 2
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
        self.lives = lives
        self.atk_delay = False
        self.atk_speed = atk_speed
        self.atk_timer = 0
        self.bullets = []
        self.max_bullets = 2
        self.bullet_size = (4, 4)
    def attack(self):
        if len(self.bullets) < self.max_bullets:
            self.bullets.append(projectile.Projectile(self, "red", [self.position[0] + self.size[0], self.position[1] + (self.size[1] - self.bullet_size[1]) / 2], self.bullet_size))
            attack_sfx = pg.mixer.Sound(f"sfx/shoot{random.randint(1,6)}.wav")
            attack_sfx.play()
    def update(self, clock, w):
        for bullet in self.bullets:
            bullet.update()
            if bullet.position[0] > w.render_width:
                self.bullets.pop(self.bullets.index(bullet))
                
        if self.atk_delay:
                self.atk_timer += clock.get_rawtime()
                if self.atk_timer >= self.atk_speed:
                    self.atk_delay = False
                    self.atk_timer = 0
    def draw(self, w):
        pg.draw.rect(w.render, self.colour, (self.position, self.size))
