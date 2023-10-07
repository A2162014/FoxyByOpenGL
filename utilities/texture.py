import pygame
from OpenGL.GL import *


# Function to render a 2D image
def render_image(image_path):
    image = pygame.image.load(image_path)
    image_data = pygame.image.tostring(image, "RGBA", 1)
    width, height = image.get_width(), image.get_height()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, glGenTextures(1))

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        width,
        height,
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        image_data,
    )

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-2, -1, 0)
    glTexCoord2f(1, 0)
    glVertex3f(2, -1, 0)
    glTexCoord2f(1, 1)
    glVertex3f(2, 1, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-2, 1, 0)
    glEnd()

    glDisable(GL_TEXTURE_2D)
