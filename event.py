import pygame as pg


class Events:
    def __init__(self):
        self.keys = []
        self.mouse_left = False
        self.mouse_right = False
        self.mouse_move = (0, 0)

    def key_down(self, key):
        return key in self.keys

    def add_key(self, key):
        self.keys.append(key)

    def remove_key(self, key):
        while key in self.keys:
            self.keys.remove(key)


def get_events(events: Events):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            quit()
        elif e.type == pg.KEYDOWN:
            events.add_key(e.key)
            if e.key == pg.K_ESCAPE:
                pg.mouse.set_visible(True)
                pg.event.set_grab(False)
        elif e.type == pg.KEYUP:
            events.remove_key(e.key)
        elif e.type == pg.MOUSEBUTTONDOWN:
            pg.mouse.set_visible(False)
            pg.event.set_grab(True)

    events.mouse_left = pg.mouse.get_pressed(num_buttons=3)[0]
    events.mouse_right = pg.mouse.get_pressed(num_buttons=3)[2]

    events.mouse_move = pg.mouse.get_rel()
