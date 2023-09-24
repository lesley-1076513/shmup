from state import GameState
import pygame as pg
import window

def poll_keys(player):
    keys = pg.key.get_pressed()
    mods = pg.key.get_mods()
    if keys[pg.K_SPACE]:
        if not player.atk_delay:
            player.attack()
            player.atk_delay = True

def handle_keyevents(event, w, game, player):
    if event.key == pg.K_ESCAPE:
        if not game.paused:
            if game.state == GameState.TITLE:
                w.running = False
            else:
                game.state = GameState.TITLE
        else:
            game.paused = not game.paused
            game.time_offset = pg.time.get_ticks() - game.time_offset

    if event.key == pg.K_RETURN and event.mod & pg.KMOD_ALT:
        window.toggle_fullscreen(w)
    if event.key == pg.K_RETURN and not event.mod & pg.KMOD_ALT:
        match game.state:
            case GameState.TITLE:
                game.state = GameState.GAME
                game.time_offset = pg.time.get_ticks()
            case GameState.GAME:
                game.paused = not game.paused
                game.time_offset = pg.time.get_ticks() - game.time_offset
            case GameState.END:
                game.state = GameState.TITLE
    # TODO: remove this
    if event.key == pg.K_1:
        player.lives -= 1
        if player.lives < 1:
            game.state = GameState.END
            game.time = (pg.time.get_ticks() - game.time_offset) / 1000