from OpenGL.GL import *
from utilities.shapes import cylinder

# Define the brown color in normalized RGB format
brown = (160 / 255.0, 90 / 255.0, 45 / 255.0)


def render_upper_leg():
    glPushMatrix()
    glTranslatef(0, 5.43, -0.5)
    cylinder.render_cylinder(0.8, 2.5, 30, brown, brown, brown)
    glPopMatrix()
