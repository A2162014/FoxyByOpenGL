import math
from OpenGL.GL import *


def render_hemisphere(radius=1.0, slices=20, stacks=10, color=(1.0, 0.0, 0.0)):
    for i in range(stacks // 2):  # Only draw the upper half
        lat0 = math.pi * (-0.5 + (i / stacks))
        lat1 = math.pi * (-0.5 + ((i + 1) / stacks))
        for j in range(slices):
            long0 = 2 * math.pi * (j / slices)
            long1 = 2 * math.pi * ((j + 1) / slices)

            x0 = radius * math.cos(long0) * math.cos(lat0)
            y0 = radius * math.sin(long0) * math.cos(lat0)
            z0 = radius * math.sin(lat0)

            x1 = radius * math.cos(long1) * math.cos(lat0)
            y1 = radius * math.sin(long1) * math.cos(lat0)
            z1 = radius * math.sin(lat0)

            x2 = radius * math.cos(long0) * math.cos(lat1)
            y2 = radius * math.sin(long0) * math.cos(lat1)
            z2 = radius * math.sin(lat1)

            x3 = radius * math.cos(long1) * math.cos(lat1)
            y3 = radius * math.sin(long1) * math.cos(lat1)
            z3 = radius * math.sin(lat1)

            glBegin(GL_TRIANGLES)
            glColor3f(*color)  # Set the vertex color
            glVertex3f(x0, y0, z0)
            glVertex3f(x1, y1, z1)
            glVertex3f(x2, y2, z2)

            glVertex3f(x2, y2, z2)
            glVertex3f(x1, y1, z1)
            glVertex3f(x3, y3, z3)
            glEnd()
