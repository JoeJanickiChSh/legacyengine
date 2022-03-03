import numpy as np
import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from pygame.locals import *
from vector3d.vector import Vector

from model import Model


def load_texture(filename: str) -> int:
    img = Image.open(filename)
    img_data = np.array(list(img.getdata()), np.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)  # GL_DECAL
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)


def init(windowSize: tuple[int]):
    gluPerspective(60, (windowSize[0] / windowSize[1]), 0.01, 100.0)

    load_texture('assets/images/atlas.png')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)


def draw(scene: list[Model]):
    glBegin(GL_TRIANGLES)
    for obj in scene:
        for face in obj:
            for v in face:
                vert = v[0]
                uv = v[1]
                glTexCoord2f(uv.x, uv.y)
                glVertex3f(vert.x, vert.y, vert.z)
    glEnd()


rotation = 0


def render(scene: list[Model]):
    global rotation
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.5, 0.5, 0.5, 1.)
    glPushMatrix()
    glRotatef(rotation, 0, 1, 0)
    glTranslate(-3, -1, 1)
    draw(scene)

    glPopMatrix()
    rotation += 0.1
    pg.display.flip()
    pg.time.wait(1)
