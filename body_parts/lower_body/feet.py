from OpenGL.GL import *

from utilities.shapes import prisim

# Define the gray color in normalized RGB format
grey = (167 / 255.0, 169 / 255.0, 173 / 255.0)


def render_foot():
    glPushMatrix()  # Save the current matrix
    prisim.render_rectangular_prism(grey)
    glPopMatrix()  # Restore the saved matrix


def render_ankle():
    glPushMatrix()
    glTranslatef(0, 0.35, -0.50)
    glScalef(1, 0.75, 0.5)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_feet():
    render_foot()

    glPushMatrix()
    # Apply translation and scaling
    glTranslatef(0.65, 0, 1.25)
    glScalef(0.35, 1, 0.25)
    # Render the toe-1
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.65, 0, 1.259)
    glScalef(0.35, 1, 0.25)
    # Render the toe-2
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    render_ankle()
