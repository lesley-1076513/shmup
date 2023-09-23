from enum import Enum
from state import GameState
import pygame as pg
import window
import draw
import input

class Game():
    def __init__(self):
        self.paused = False
        self.debug = True
        self.state = GameState.TITLE
        self.fps = 60
        self.font_size = 16
        self.render_col = (150, 150, 150)
        self.screen_col = (100, 100, 100)

pg.init()
w = window.Window()
clock = pg.time.Clock()
game = Game()
font = pg.font.Font("gfx/alagard.ttf", game.font_size)

def run():
    while w.running:
        if game.debug:
            pg.display.set_caption(f"{w.title} - {str(int(clock.get_fps()))} fps")

        input.poll_keys()

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    w.running = False
                case pg.VIDEORESIZE:
                    window.scale_window(w)
                case pg.KEYDOWN:
                    input.handle_keyevents(event, w, game)

        if game.paused:
            draw.pause(w, game, font)
        else:
            draw.draw(w, game, font)
        clock.tick(game.fps)
    pg.quit()
