import pygame as pg
from state import GameState

def draw(w, game, font):
    w.render.fill(game.render_col)
    w.screen.fill(game.screen_col)
    
    match game.state:
        case GameState.TITLE:
            screen_text = "title screen"
        case GameState.GAME:
            screen_text = "game screen"
        case GameState.END:
            screen_text = "end screen"

    text = font.render(screen_text, False, "yellow")
    w.render.blit(text, center(w, game, screen_text))
    w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
    pg.display.flip()

def center(w, game, text):
    return ((w.render_width - len(text) * game.font_size // 2) // 2, (w.render_height - game.font_size // 2) // 2)
