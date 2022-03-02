import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init(windowSize: tuple[int], name: str):
    pg.init()
    pg.display.set_caption(name)
    pg.display.set_mode(windowSize, DOUBLEBUF | OPENGL)

    pg.mouse.set_visible(False)
    pg.event.set_grab(True)
