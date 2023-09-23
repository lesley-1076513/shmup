import pygame as pg
from state import GameState

def draw(w, game, font):
    w.render.fill(game.render_col)
    w.screen.fill(game.screen_col)
    
    match game.state:
        case GameState.TITLE:
            primary_text = "Hiscore: 0"
            secondary_text = "Start (enter)"
            tertiary_text = "Quit (escape)"
        case GameState.GAME:
            primary_text = "Lives: 0"
            secondary_text = "Score: 0"
            tertiary_text = "Time: 0"
        case GameState.END:
            primary_text = "Game Over"
            secondary_text = "Score: 0"
            tertiary_text = "Time: 0"

    text1 = font.render(primary_text, False, "yellow")
    text2 = font.render(secondary_text, False, "yellow")
    text3 = font.render(tertiary_text, False, "yellow")

    match game.state:
        case GameState.TITLE | GameState.END:
            w.render.blit(text1, center_width(w, game, primary_text, 3))
            w.render.blit(text2, center_width(w, game, secondary_text, 5))
            w.render.blit(text3, center_width(w, game, tertiary_text, 7))
        case GameState.GAME:
            w.render.blit(text1, (1*game.font_size, 0))
            w.render.blit(text2, center_width(w, game, secondary_text, 0))
            w.render.blit(text3, (15*game.font_size, 0))

    w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
    pg.display.flip()

def pause(w, game, font):
    pause_text = "Paused"
    text = font.render(pause_text, False, "yellow")
    w.render.blit(text, center(w, game, pause_text))
    w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
    pg.display.flip()

def center_height(w, game, text, width):
    return (width * game.font_size, (w.render_height - game.font_size // 2) // 2)

def center_width(w, game, text, height):
    return ((w.render_width - len(text) * game.font_size // 2) // 2, height * game.font_size)

def center(w, game, text):
    return ((w.render_width - len(text) * game.font_size // 2) // 2, (w.render_height - game.font_size // 2) // 2)
