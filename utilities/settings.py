from OpenGL.GL import *


# Initialize OpenGL settings
def init_opengl(window_size):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = window_size[0] / window_size[1]
    glFrustum(-aspect_ratio, aspect_ratio, -1, 1, 1, 50)  # Set up perspective projection
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering
    glDepthFunc(GL_LESS)
