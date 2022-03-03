from vector3d.vector import Vector


class Box:
    def __init__(self, position: Vector, size: Vector):
        self.position = position
        self.size = size

    def collision(self, other) -> bool:
        if other.position.x - other.size.x - self.size.x < self.position.x < other.position.x + other.size.x + self.size.x:
            if other.position.y - other.size.y - self.size.y < self.position.y < other.position.y + other.size.y + self.size.y:
                if other.position.z - other.size.z - self.size.z < self.position.z < other.position.z + other.size.z + self.size.z:
                    return True
        return False
