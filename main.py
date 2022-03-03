import math

import pygame as pg
from vector3d.vector import Vector

import event
import obj
import render
import window
from camera import Camera


def main():
    WINDOW_SIZE = (1080, 720)
    window.init(WINDOW_SIZE, "Game")
    render.init(WINDOW_SIZE)
    events = event.Events()

    test_scene = obj.parse('assets/models/forest.obj')
    skybox = obj.parse('assets/models/skybox.obj')
    skybox.scale *= 500
    skybox.shade = False
    scene = [test_scene, skybox]

    camera = Camera(Vector(0, 1, -0.8), Vector(0, 0, 0))
    velocity = Vector(0, 0, 0)

    while True:
        event.get_events(events)
        render.render(scene, camera)

        camera.rotation.y += events.mouse_move[0] / 500.0
        camera.rotation.x += events.mouse_move[1] / 500.0

        rotation = Vector(
            math.sin(camera.rotation.y),
            -math.cos(camera.rotation.y)
        ) * 0.001

        if events.key_down(pg.K_w):
            velocity.x += rotation.x
            velocity.z += rotation.y
        if events.key_down(pg.K_s):
            velocity.x -= rotation.x
            velocity.z -= rotation.y
        if events.key_down(pg.K_a):
            velocity.x += rotation.y
            velocity.z -= rotation.x
        if events.key_down(pg.K_d):
            velocity.x -= rotation.y
            velocity.z += rotation.x
        if events.key_down(pg.K_SPACE):
            velocity.y += 0.001
        if events.key_down(pg.K_LSHIFT):
            velocity.y -= 0.001

        camera.position += velocity

        skybox.position = camera.position * 1.0

        velocity *= 0.96


if __name__ == '__main__':
    main()
