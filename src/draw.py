import pygame as pg
from state import GameState

def draw(w, game, font, player):
    w.screen.fill(game.screen_col)
    w.render.fill(game.render_col)
    
    match game.state:
        case GameState.TITLE:
            primary_text = f"Hiscore: {game.hiscore}"
            secondary_text = "Start (enter)"
            tertiary_text = "Quit (escape)"
        case GameState.GAME:
            primary_text = f"Lives: {player.lives}"
            secondary_text = f"Score: {game.score}"
            timer = int((pg.time.get_ticks() - game.time_offset) / 1000)
            if timer > game.timer_too_long:
                tertiary_text = "Too long"
            else:
                tertiary_text = f"Time: {timer}"

            player.draw(w)
            for bullet in player.bullets:
                bullet.draw(w)
                
        case GameState.END:
            primary_text = "Game Over"
            secondary_text = f"Score: {game.score}"
            tertiary_text = f"Time: {game.time}"

    text1 = font.render(primary_text, False, "yellow")
    text2 = font.render(secondary_text, False, "yellow")
    text3 = font.render(tertiary_text, False, "yellow")

    match game.state:
        case GameState.TITLE | GameState.END:
            w.render.blit(text1, center_width(w, game, primary_text, 3))
            w.render.blit(text2, center_width(w, game, secondary_text, 5))
            w.render.blit(text3, center_width(w, game, tertiary_text, 7))
        case GameState.GAME:
            w.render.blit(text1, (0, 0))
            w.render.blit(text2, center_width(w, game, secondary_text, 0))
            w.render.blit(text3, (15*game.font_size, 0))

    w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
    pg.display.flip()

def pause(w, game, font):
    w.screen.fill(game.screen_col)
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
