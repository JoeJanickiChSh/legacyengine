import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init(windowSize: tuple[int]):
    gluPerspective(60, (windowSize[0] / windowSize[1]), 0.01, 100.0)
    glEnable(GL_DEPTH_TEST)


def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.5, 0.5, 0.5, 1.)
    glPushMatrix()
    glPopMatrix()
    pg.display.flip()
    pg.time.wait(1)
