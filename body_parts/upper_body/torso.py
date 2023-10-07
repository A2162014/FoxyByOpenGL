from OpenGL.GL import *
from utilities.shapes import hemisphere, cylinder

# Define the red and peach color in normalized RGB format
red = (251 / 255.0, 75 / 255.0, 44 / 255.0)
peach = (245 / 255.0, 189 / 255.0, 173 / 255.0)

# Set the fixed rotation angle (in degrees)
hemisphere_rotation_angle = 90


def render_torso():
    glPushMatrix()
    glTranslatef(-1.5, 10.4, -0.5)
    glScalef(1, 1, 0.5)
    cylinder.render_cylinder(2, 6, 30, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.5, 10.4, 0.1)
    glScalef(1, 1, 0.3)
    cylinder.render_cylinder(1.6, 6, 30, peach, peach, peach)
    glPopMatrix()

    glPushMatrix()
    glRotatef(hemisphere_rotation_angle, 1, 0, 0)
    glTranslatef(-1.5, -0.5, -13.4)
    glScalef(1, 0.5, 0.2)
    hemisphere.render_hemisphere(2, 30, 30, red)
    glPopMatrix()
