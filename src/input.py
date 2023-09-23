from state import GameState
import pygame as pg
import window

def poll_keys():
    keys = pg.key.get_pressed()
    mods = pg.key.get_mods()
    # if keys[pg.K_SPACE]:

def handle_keyevents(event, w, game):
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