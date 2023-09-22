import pygame as pg
import os

class Window():
    def __init__(self):
        self.title = "Speed Game"
        self.start_fullscreen = True
        self.aspect_x = 16
        self.aspect_y = 9
        self.aspect_scale = 20
        self.render_width = self.aspect_x * self.aspect_scale
        self.render_height = self.aspect_y * self.aspect_scale
        self.render_scale = calc_render_scale(self)
        self.screen_width = self.render_width * self.render_scale
        self.screen_height = self.render_height * self.render_scale
        self.flags = pg.RESIZABLE
        self.fullscreen = False
        self.running = True
        self.render = pg.Surface([self.render_width, self.render_height])
        if self.start_fullscreen:
            toggle_fullscreen(self)
        elif not self.start_fullscreen:
            self.screen = pg.display.set_mode((self.screen_width, self.screen_height), self.flags)
            pg.display.set_caption(self.title)

def calc_render_scale(w):
    size = pg.display.get_desktop_sizes()
    width_scale = size[0][0] // w.render_width - 1
    height_scale = size[0][1] // w.render_height - 1
    if width_scale < 1 and height_scale < 1:
        return 1
    return width_scale if width_scale > height_scale else height_scale

def calc_scale(w):
    surface = pg.display.get_surface()
    width = surface.get_width() // w.aspect_x
    height = surface.get_height() // w.aspect_y
    return height if (width * w.aspect_x > height * w.aspect_y) else width

def scale_window(w):
    scaled = calc_scale(w);
    w.screen_width = w.aspect_x * scaled;
    w.screen_height = w.aspect_y * scaled;

def toggle_fullscreen(w):
    w.fullscreen = not w.fullscreen
    w.flags = w.flags ^ pg.NOFRAME
    size = pg.display.get_desktop_sizes()
    pg.display.quit()
    if w.fullscreen:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
        w.screen = pg.display.set_mode((size[0][0], size[0][1]), w.flags)
    if not w.fullscreen:
        # os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (size[0][0] // 2 - w.render_width * w.render_scale // 2, size[0][1] // 2 - w.render_height * w.render_scale // 2)
        os.environ['SDL_VIDEO_CENTERED'] = "1"
        w.screen = pg.display.set_mode((w.render_width * w.render_scale, w.render_height * w.render_scale), w.flags)
    pg.display.init()
    pg.display.set_caption(w.title)
    scale_window(w)
    