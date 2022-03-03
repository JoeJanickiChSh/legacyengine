import math
import numpy as np
import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from pygame.locals import *
from vector3d.vector import Vector

from camera import Camera
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
    gluPerspective(60, (windowSize[0] / windowSize[1]), 0.01, 1000.0)

    load_texture('assets/images/atlas.png')

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)


def get_normal(v1: Vector, v2: Vector, v3: Vector) -> Vector:
    u = (v2).normalize() - (v1).normalize()
    v = (v3).normalize() - (v1).normalize()
    return Vector((u.y * v.z) - (u.z * v.y), (u.z * v.x) - (u.x * v.z),
                  (u.x * v.y) - (u.y * v.x)).normalize()


def dot(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def shading(normal: Vector, light_dir: Vector) -> float:
    return dot(normal, light_dir) / 3.0 + 0.8


def draw(scene: list[Model]):
    glBegin(GL_TRIANGLES)
    for obj in scene:
        for face in obj:

            normal = get_normal(face[0][0], face[1][0], face[2][0])
            shade = shading(normal, Vector(1, 1, 1).normalize())
            for vert, uv in face:

                vert = Vector(vert.x * obj.scale.x,
                              vert.y * obj.scale.y, vert.z * obj.scale.z)
                vert = vert + obj.position
                if obj.shade:
                    glColor3f(shade, shade, shade)
                else:
                    glColor3f(1, 1, 1)
                glTexCoord2f(uv.x, uv.y)
                glVertex3f(vert.x, vert.y, vert.z)
    glEnd()


rotation = 0


def render(scene: list[Model], camera: Camera):
    global rotation
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.5, 0.5, 0.5, 1.)
    glPushMatrix()

    glRotate(math.degrees(camera.rotation.z), 0, 0, 1)
    glRotate(math.degrees(camera.rotation.x), 1, 0, 0)
    glRotate(math.degrees(camera.rotation.y), 0, 1, 0)

    glTranslate(-camera.position.x, -camera.position.y, -camera.position.z)

    draw(scene)

    glPopMatrix()
    rotation += 0.1
    pg.display.flip()
    pg.time.wait(1)
