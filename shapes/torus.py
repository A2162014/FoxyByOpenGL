import math
from OpenGL.GL import *


def render_torus(color):
    glColor3f(*color)

    # Set the parameters for the torus
    R = 1.2  # Major radius
    r = 0.3  # Minor radius
    num_slices = 30
    num_segments = 30

    for i in range(num_slices):
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            theta = (2.0 * math.pi * i / num_slices)
            phi = (2.0 * math.pi * j / num_segments)
            x = (R + r * math.cos(phi)) * math.cos(theta)
            y = (R + r * math.cos(phi)) * math.sin(theta)
            z = r * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)

            theta = (2.0 * math.pi * (i + 1) / num_slices)
            x = (R + r * math.cos(phi)) * math.cos(theta)
            y = (R + r * math.cos(phi)) * math.sin(theta)
            z = r * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)
        glEnd()


def render_two_thirds_torus(color, R=1.2, r=0.3):
    glColor3f(*color)

    # Set the parameters for the torus
    major_radius = R  # Major radius
    minor_radius = r  # Minor radius
    num_slices = 30  # Number of slices (adjust as needed for the desired portion)
    num_segments = 30

    for i in range(num_slices // 3, num_slices):  # Iterating for 3/4th of the torus
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            theta = (2.0 * math.pi * i / num_slices)
            phi = (2.0 * math.pi * j / num_segments)
            x = (major_radius + minor_radius * math.cos(phi)) * math.cos(theta)
            y = (major_radius + minor_radius * math.cos(phi)) * math.sin(theta)
            z = minor_radius * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)

            theta = (2.0 * math.pi * (i + 1) / num_slices)
            x = (major_radius + minor_radius * math.cos(phi)) * math.cos(theta)
            y = (major_radius + minor_radius * math.cos(phi)) * math.sin(theta)
            z = minor_radius * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)
        glEnd()


def render_one_fourth_torus(color, R=1.2, r=0.3):
    glColor3f(*color)

    # Set the parameters for the torus
    major_radius = R  # Major radius
    minor_radius = r  # Minor radius
    num_slices = 30  # Total number of slices
    num_segments = 30

    for i in range(num_slices // 4):  # Iterating for 1/4 of the torus
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            theta = (2.0 * math.pi * i / num_slices)
            phi = (2.0 * math.pi * j / num_segments)
            x = (major_radius + minor_radius * math.cos(phi)) * math.cos(theta)
            y = (major_radius + minor_radius * math.cos(phi)) * math.sin(theta)
            z = minor_radius * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)

            theta = (2.0 * math.pi * (i + 1) / num_slices)
            x = (major_radius + minor_radius * math.cos(phi)) * math.cos(theta)
            y = (major_radius + minor_radius * math.cos(phi)) * math.sin(theta)
            z = minor_radius * math.sin(phi)

            glNormal3f(x, y, z)
            glVertex3f(x, y, z)
        glEnd()
