from OpenGL.GL import *
from utilities.shapes import prisim, cylinder

# Define the brown color in normalized RGB format
brown = (160 / 255.0, 90 / 255.0, 45 / 255.0)


def render_upper_cylinder():
    glPushMatrix()
    glTranslatef(1.5, 7.05, -0.51)
    glScalef(1, 0.7, 0.4)
    cylinder.render_cylinder(2.2, 1, 30, brown, brown, brown)
    glPopMatrix()


def render_lower_cuboid():
    glPushMatrix()
    glTranslatef(1.5, 6.5, -0.5)
    glScalef(0.7, 2, 0.7)
    prisim.render_rectangular_prism(brown)
    glPopMatrix()


def render_groin():
    render_upper_cylinder()
    render_lower_cuboid()
