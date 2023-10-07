from OpenGL.GL import *
from utilities.shapes import torus, cylinder

# Define the gray color in normalized RGB format
grey = (167 / 255.0, 169 / 255.0, 173 / 255.0)

# Set the fixed rotation angle (in degrees)
torus_rotation_angle = 90


def render_lower_torus():
    glPushMatrix()
    glRotatef(torus_rotation_angle, 1, 0, 0)
    glScalef(0.4, 0.4, 0.4)
    glTranslatef(0, -1.3, -1.4)
    torus.render_torus(grey)
    glPopMatrix()


def render_upper_torus():
    glPushMatrix()
    glRotatef(torus_rotation_angle, 1, 0, 0)
    glScalef(0.4, 0.4, 0.4)
    glTranslatef(0, -1.3, -10.2)
    torus.render_torus(grey)
    glPopMatrix()


def render_lower_leg():
    render_lower_torus()

    glPushMatrix()
    # Render the leg part of foot – 2
    glTranslatef(0, 1.4, -0.5)
    cylinder.render_cylinder(0.4, 2, 30, grey, grey, grey)
    glPopMatrix()

    glPushMatrix()
    # Render the leg part of foot – 3
    glTranslatef(0, 2.6, -0.5)
    cylinder.render_cylinder(0.4, 2, 30, grey, grey, grey)
    glPopMatrix()

    glPushMatrix()
    # Render the leg part of foot – 4
    glTranslatef(0, 3.5, -0.5)
    cylinder.render_cylinder(0.4, 1, 30, grey, grey, grey)
    glPopMatrix()

    render_upper_torus()
