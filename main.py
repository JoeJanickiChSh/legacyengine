import math
from copy import deepcopy

import pygame as pg
from vector3d.vector import Vector

import event
import obj
import render
import window
from box import Box
from camera import Camera


def scene_collision(camera_box: Box, collisions: list[Box]):
    for box in collisions:
        if camera_box.collision(box):
            return True
    return False


def main():
    WINDOW_SIZE = (1080, 720)
    window.init(WINDOW_SIZE, "Game")
    render.init(WINDOW_SIZE)
    events = event.Events()

    test_scene = obj.parse('assets/models/moon.obj')
    skybox = obj.parse('assets/models/moon_skybox.obj')
    skybox.scale *= 500
    skybox.shade = False

    dcube = obj.parse('assets/models/debug.obj')

    scene = [test_scene, skybox]

    collisions = []

    for f in test_scene:
        max_point = Vector(-1, -1, -1) * 1000
        min_point = Vector(1, 1, 1) * 1000
        for v, uv in f:
            if v.x > max_point.x:
                max_point.x = v.x
            if v.x < min_point.x:
                min_point.x = v.x
            if v.y > max_point.y:
                max_point.y = v.y
            if v.y < min_point.y:
                min_point.y = v.y
            if v.z > max_point.z:
                max_point.z = v.z
            if v.z < min_point.z:
                min_point.z = v.z

        mid_point = (max_point + min_point) * 0.5
        size = (max_point - min_point) * 0.5
        collisions.append(Box(mid_point, size))

    camera = Camera(Vector(), Vector(0, 0, 0))
    camera_box = Box(Vector(0, 2, 0), Vector(1, 2, 1))
    velocity = Vector(0, 0, 0)

    while True:
        event.get_events(events)
        render.render(scene, camera)

        camera.rotation.y += events.mouse_move[0] / 500.0
        camera.rotation.x += events.mouse_move[1] / 500.0
        camera.rotation.x = min(math.pi/2, max(-math.pi/2, camera.rotation.x))

        rotation = Vector(
            math.sin(camera.rotation.y),
            -math.cos(camera.rotation.y)
        ) * 0.0011
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

        velocity.y -= 0.0003

        camera_box.position.x += velocity.x
        if scene_collision(camera_box, collisions):
            camera_box.position.x -= velocity.x
            velocity.x = 0
        camera_box.position.y += velocity.y
        if scene_collision(camera_box, collisions):
            camera_box.position.y -= velocity.y
            velocity.y = 0
            if events.key_down(pg.K_SPACE):
                velocity.y = 0.03
        camera_box.position.z += velocity.z
        if scene_collision(camera_box, collisions):
            camera_box.position.z -= velocity.z
            velocity.z = 0

        velocity.x *= 0.96
        velocity.z *= 0.96

        skybox.position = camera_box.position * 1.0

        camera.position = camera_box.position * 1.0

        if scene_collision(camera_box, collisions):
            print("Collision")


if __name__ == '__main__':
    main()
