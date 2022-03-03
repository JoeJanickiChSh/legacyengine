from vector3d.vector import Vector


class Camera:
    def __init__(self, position: Vector, rotation: Vector):
        self.position = position
        self.rotation = rotation
