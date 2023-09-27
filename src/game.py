from enum import Enum
from state import GameState
import pygame as pg
import window
import draw
import input
import entity

class Game():
    def __init__(self):
        self.paused = False
        self.debug = True
        self.state = GameState.TITLE
        self.fps = 60
        self.font_size = 16
        self.render_col = (0, 0, 0)
        self.screen_col = (45, 56, 58)
        self.score = 0
        self.hiscore = 0
        self.time_offset = 0
        self.time = 0
        self.timer_too_long = 9999

pg.init()
w = window.Window()
clock = pg.time.Clock()
game = Game()
font = pg.font.Font("gfx/alagard.ttf", game.font_size)
player = entity.Entity("white", [0, w.render_height/2], (16, 16), 3, 60)

def run():
    while w.running:
        if game.debug:
            pg.display.set_caption(f"{w.title} - {str(int(clock.get_fps()))} fps")

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    w.running = False
                case pg.VIDEORESIZE:
                    window.scale_window(w)
                case pg.KEYDOWN:
                    input.handle_keyevents(event, w, game, player)

        if game.state == GameState.GAME and not game.paused:
            player.update(clock, w)
            input.poll_keys(player)

        if game.paused:
            draw.pause(w, game, font)
        else:
            draw.draw(w, game, font, player)
            
        clock.tick(game.fps)
    pg.quit()
