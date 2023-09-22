from enum import Enum
import pygame as pg

class GameState(Enum):
    TITLE = 1
    GAME = 2
    END = 3

class Game():
    def __init__(self):
        self.title = "Speed Game"
        self.state = GameState.TITLE
        self.fps_rate = 60
        self.screen_width = 1024
        self.screen_height = 768
        self.title_bg = (100, 100, 100)
        self.game_bg = (0, 0, 0)
        self.end_bg = (255, 0, 0)

pg.init()
clock = pg.time.Clock()
game = Game()
pg.display.set_caption(game.title)
surface = pg.display.set_mode((game.screen_width, game.screen_height))

def run():
    running = True
    while running:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    running = False
                case pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
                    if event.key == pg.K_RETURN:
                        match game.state:
                            case GameState.TITLE:
                                game.state = GameState.GAME
                            case GameState.GAME:
                                game.state = GameState.END
                            case GameState.END:
                                game.state = GameState.TITLE

        match game.state:
            case GameState.TITLE:
                surface.fill(game.title_bg)
            case GameState.GAME:
                surface.fill(game.game_bg)
            case GameState.END:
                surface.fill(game.end_bg)

        pg.display.flip()
        clock.tick(game.fps_rate)
        