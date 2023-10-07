from OpenGL.GL import *
from utilities.shapes import cylinder

grey = (167 / 255.0, 169 / 255.0, 173 / 255.0)


def render_neck():
    glPushMatrix()
    glTranslatef(-1.481, 14.2, -0.442)
    glRotatef(20, 1, 0, 0)
    cylinder.render_cylinder(0.2, 1.45, 30, grey, grey, grey)
    glPopMatrix()
