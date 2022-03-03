from vector3d.vector import Vector

from model import Model


def parse(filename: str) -> Model:
    verts = []
    uvs = []
    faces = []

    with open(filename, 'r') as fp:
        lines = fp.read().split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i].split()

    for line in lines:
        if len(line) > 0:
            if line[0] == 'v':
                x = float(line[1])
                y = float(line[2])
                z = float(line[3])
                verts.append(Vector(x, y, z))
            elif line[0] == 'vt':
                x = float(line[1])
                y = float(line[2])
                # Possible bug somewhere else that inverts the y-axis of UVs
                uvs.append(Vector(x, 1-y))
            elif line[0] == 'f':
                face = []
                for v in line[1:]:
                    split = v.split('/')
                    face.append(tuple(map(lambda x: int(x)-1, split)))
                faces.append(face)
    return Model(verts, uvs, faces)
