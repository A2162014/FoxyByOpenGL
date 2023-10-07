import numpy as np
from OpenGL.GL import *


def render_cone(cone_color, radius, height):
    # Define the number of segments
    num_segments = 50

    # Calculate the base vertices of the cone
    theta = np.linspace(0, 2 * np.pi, num_segments)
    x_base = radius * np.cos(theta)
    y_base = radius * np.sin(theta)
    z_base = np.zeros(num_segments)

    # Define the vertices of the cone
    vertices = np.vstack((x_base, y_base, z_base)).T
    vertices = np.vstack((vertices, [0, 0, height]))  # Apex
    vertices = np.vstack((vertices, [0, 0, 0]))  # Center of the base

    # Define the indices of the cone's faces
    cone_indices = []
    for i in range(num_segments):
        cone_indices.extend([i, (i + 1) % num_segments, num_segments])

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Set fill mode
    glColor3f(*cone_color)  # Set color for the cone faces
    glBegin(GL_TRIANGLES)
    for i in cone_indices:
        glVertex3fv(vertices[i])
    glEnd()
