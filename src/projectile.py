import pygame as pg

class Projectile():
    def __init__(self, entity, col, pos, size):
        self.entity = entity
        self.colour = col
        self.position = pos
        self.size = size
        self.speed = 3
        self.surface = pg.Surface(self.size)
        self.rect = self.surface.get_rect()
    def update(self):
        self.position[0] -= self.speed            
    def draw(self, w):
        pg.draw.rect(w.render, self.colour, (self.position, self.size))

