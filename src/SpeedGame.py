import pygame as pg

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BG_COLOR = (100, 100, 100)
FPS_RATE = 60

pg.init()
pg.display.set_caption("Speed Game")
clock = pg.time.Clock()
surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                running = False
            case pg.KEYDOWN:
                match event.key:
                    case pg.K_ESCAPE:
                        running = False

    surface.fill(BG_COLOR)
    pg.display.flip()
    clock.tick(FPS_RATE)