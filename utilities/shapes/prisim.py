from OpenGL.GL import *


def render_rectangular_prism(color, border=True):
    # Define cuboid vertices and edges
    vertices = [
        [-1, -0.32, -1],  # Vertex 0 – bottom-left-back corner
        [1, -0.32, -1],  # Vertex 1 – bottom-right-back corner
        [1, 0.1, -1],  # Vertex 2 – bottom-right-front corner
        [-1, 0.1, -1],  # Vertex 3 – bottom-left-front corner
        [-1, -0.32, 1],  # Vertex 4 – top-left-back corner
        [1, -0.32, 1],  # Vertex 5 – top-right-back corner
        [1, 0.1, 1],  # Vertex 6 – top-right-front corner
        [-1, 0.1, 1]  # Vertex 7 – top-left-front corner
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Front face edges
        (4, 5), (5, 6), (6, 7), (7, 4),  # Back face edges
        (0, 4), (1, 5), (2, 6), (3, 7)  # Connecting edges
    ]

    # Define cube faces
    faces = [
        [0, 1, 2, 3],  # Front face
        [4, 5, 6, 7],  # Back face
        [1, 5, 6, 2],  # Right face
        [0, 4, 7, 3],  # Left face
        [3, 2, 6, 7],  # Top face
        [0, 1, 5, 4]  # Bottom face
    ]

    # Render the cuboid faces with gray color
    for _, face in enumerate(faces):
        glColor3f(*color)  # Set the color
        glBegin(GL_QUADS)
        for vertex in face:
            glVertex3fv(vertices[vertex])
        glEnd()

    if border:
        # Set the line width for the cube's border
        glLineWidth(3.0)  # You can adjust the width as needed

        glColor3f(0, 0, 0)  # Set the color
        # Render the cube edges with black color
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
