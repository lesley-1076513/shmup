from enum import Enum
import pygame as pg
import window
import draw
from state import GameState

class Game():
    def __init__(self):
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
# font = pg.font.Font("gfx/alagard.ttf", game.font_size)
font = pg.font.Font("gfx/Mario-Kart-DS.ttf", game.font_size)

def run():
    while w.running:
        if game.debug:
            pg.display.set_caption(f"Speed Game - {str(int(clock.get_fps()))} fps")

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    w.running = False
                case pg.VIDEORESIZE:
                    window.scale_window(w)
                case pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        w.running = False
                    if event.key == pg.K_RETURN and event.mod & pg.KMOD_ALT:
                        window.toggle_fullscreen(w)
                    if event.key == pg.K_RETURN and not event.mod & pg.KMOD_ALT:
                        match game.state:
                            case GameState.TITLE:
                                game.state = GameState.GAME
                            case GameState.GAME:
                                game.state = GameState.END
                            case GameState.END:
                                game.state = GameState.TITLE
                    if event.key == pg.K_SPACE:
                        coin_sfx = pg.mixer.Sound("sfx/coin1.wav")
                        coin_sfx.play()

        draw.draw(w, game, font)
        clock.tick(game.fps)
    pg.quit()
