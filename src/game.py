from enum import Enum
import pygame as pg
import window

class GameState(Enum):
    TITLE = 1
    GAME = 2
    END = 3

class Game():
    def __init__(self):
        self.running = True
        self.state = GameState.TITLE
        self.fps = 60
        self.debug = True
        self.bg_color = (150, 150, 150)
        self.title_bg = (100, 100, 100)
        self.game_bg = (0, 0, 0)
        self.end_bg = (255, 0, 0)

pg.init()
w = window.Window()
clock = pg.time.Clock()
# font = pg.font.Font("gfx/alagard.ttf", w.font_size)
font = pg.font.Font("gfx/Mario-Kart-DS.ttf", w.font_size)
game = Game()

def run():
    while game.running:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    game.running = False
                case pg.VIDEORESIZE:
                    window.scale_window(w)
                case pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        game.running = False
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

        w.screen.fill((game.bg_color))
        match game.state:
            case GameState.TITLE:
                w.render.fill(game.title_bg)
                text = font.render("titlescreen", False, "yellow")
            case GameState.GAME:
                w.render.fill(game.game_bg)
                text = font.render("gamescreen", False, "yellow")
            case GameState.END:
                w.render.fill(game.end_bg)
                text = font.render("endscreen", False, "yellow")
            
        if game.debug:
            pg.display.set_caption(f"Speed Game - {str(int(clock.get_fps()))} fps")

        w.render.blit(text, (0, 0))
        w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
        pg.display.flip()
        clock.tick(game.fps)
    pg.quit()
