from vector3d.vector import Vector


class Model:
    def __init__(self, verts: list[Vector], uvs: list[Vector], faces: list[list[tuple[int]]]):
        self.verts = verts
        self.uvs = uvs
        self.faces = faces
        self.position = Vector(0, 0, 0)
        self.scale = Vector(1, 1, 1)
        self.shade = True

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.faces):
            face = self.faces[self.index]
            self.index += 1
            out_list = []
            for vert, uv in face:
                out_list.append((self.verts[vert], self.uvs[uv]))
            return out_list
        else:
            raise StopIteration
