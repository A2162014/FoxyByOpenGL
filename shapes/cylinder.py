import math
from OpenGL.GL import *

black = (0, 0, 0)


def render_cylinder(radius, height, num_slices, top_color, bottom_color, side_color, border_color=black):
    r = radius
    h = height
    n = num_slices
    delta_angle = 2 * math.pi / n
    cos_values = [r * math.cos(i * delta_angle) for i in range(n + 1)]
    sin_values = [r * math.sin(i * delta_angle) for i in range(n + 1)]

    # Draw the top and bottom circles
    glColor(*top_color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0, h / 2.0, 0)
    for i in range(n + 1):
        glVertex(cos_values[i], h / 2.0, sin_values[i])
    glEnd()

    glColor(*bottom_color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex(0, -h / 2.0, 0)
    for i in range(n + 1):
        glVertex(cos_values[i], -h / 2.0, sin_values[i])
    glEnd()

    # Draw the sides of the cylinder
    glColor(*side_color)
    glBegin(GL_QUAD_STRIP)
    for i in range(n + 1):
        glVertex(cos_values[i], h / 2.0, sin_values[i])
        glVertex(cos_values[i], -h / 2.0, sin_values[i])
    glEnd()

    # Draw the black border for the top and bottom circles
    glColor(border_color)  # Black color for the border
    glLineWidth(3.0)  # Set the line width for the border
    glBegin(GL_LINE_LOOP)
    for i in range(n + 1):
        glVertex(cos_values[i], h / 2.0, sin_values[i])
    glEnd()

    glBegin(GL_LINE_LOOP)
    for i in range(n + 1):
        glVertex(cos_values[i], -h / 2.0, sin_values[i])
    glEnd()

    # Draw the black border for the sides of the cylinder
    glBegin(GL_LINE_STRIP)
    for i in range(n + 1):
        glVertex(cos_values[i], h / 2.0, sin_values[i])
    glEnd()
