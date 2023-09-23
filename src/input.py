from state import GameState
import pygame as pg
import window
import random

def poll_keys():
    keys = pg.key.get_pressed()
    mods = pg.key.get_mods()
    # if keys[pg.K_SPACE]:

def handle_keyevents(event, w, game):
    if event.key == pg.K_ESCAPE:
        if not game.paused:
            if game.state == GameState.TITLE:
                w.running = False
            else:
                game.state = GameState.TITLE
    if event.key == pg.K_RETURN and event.mod & pg.KMOD_ALT:
        window.toggle_fullscreen(w)
    if event.key == pg.K_RETURN and not event.mod & pg.KMOD_ALT:
        match game.state:
            case GameState.TITLE:
                game.state = GameState.GAME
            case GameState.GAME:
                if game.paused:
                    game.paused = False
                else:
                    game.paused = True
            case GameState.END:
                game.state = GameState.TITLE
    if event.key == pg.K_SPACE:
        coin_sfx = pg.mixer.Sound(f"sfx/explosion{random.randint(1,3)}.wav")
        coin_sfx.play()