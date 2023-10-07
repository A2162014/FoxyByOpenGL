from OpenGL.GL import *
from utilities.shapes import sphere

red = (251 / 255.0, 76 / 255.0, 43 / 255.0)


def render_base():
    glPushMatrix()
    glTranslatef(-1.473, 15.85, -0.58)
    glScalef(1, 1, 1)
    sphere.render_sphere(1.58, 30, 30, red)
    glPopMatrix()
