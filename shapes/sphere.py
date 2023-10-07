import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *


def render_sphere(radius=1.0, num_segments=30, num_rings=30, color=(1.0, 0.0, 0.0)):
    # Lists to store sphere vertices and indices
    vertices = []
    indices = []

    # Generate vertices and indices for the sphere
    for i in range(num_rings + 1):
        theta = i * np.pi / num_rings
        sin_theta = np.sin(theta)
        cos_theta = np.cos(theta)

        for j in range(num_segments + 1):
            phi = j * 2 * np.pi / num_segments
            sin_phi = np.sin(phi)
            cos_phi = np.cos(phi)

            x = radius * sin_theta * cos_phi
            y = radius * sin_theta * sin_phi
            z = radius * cos_theta

            vertices.extend([x, y, z])

    for i in range(num_rings):
        for j in range(num_segments):
            v0 = i * (num_segments + 1) + j
            v1 = v0 + num_segments + 1
            v2 = v0 + 1
            v3 = v1 + 1

            indices.extend([v0, v1, v2])
            indices.extend([v2, v1, v3])

    # Convert vertices and indices to NumPy arrays
    vertices = np.array(vertices, dtype=np.float32)
    indices = np.array(indices, dtype=np.uint32)

    # Create a Vertex Buffer Object (VBO) for vertices
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

    # Create a Vertex Array Object (VAO) to encapsulate vertex attribute setup
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)

    # Create an Element Buffer Object (EBO) for indices
    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    # Bind the VAO and set the color for rendering
    glBindVertexArray(vao)
    glColor3f(*color)

    # Draw the sphere using indexed triangles
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # Unbind the VAO to restore the default state
    glBindVertexArray(0)
