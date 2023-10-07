import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from utilities import settings, texture

import head
import lower_body
import upper_body

# Initialize camera settings
camera_x, camera_y = 0, 0
camera_speed = 0.15

# Initialize camera rotation angles
camera_rotation_x = 0
camera_rotation_y = 0

# Initialize mouse interaction variables
mouse_pressed = False
last_mouse_pos = None


# Get 3D coordinates of the mouse cursor
def get_3d_coordinates():
    viewport = glGetIntegerv(GL_VIEWPORT)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_z = glReadPixels(mouse_x, viewport[3] - mouse_y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)
    mouse_x, mouse_y, mouse_z = gluUnProject(mouse_x, viewport[3] - mouse_y, mouse_z)
    return mouse_x, mouse_y, mouse_z


# Handle user input
def handle_input(zoom, zoom_speed):
    global camera_x, camera_y, camera_rotation_x, camera_rotation_y, mouse_pressed, last_mouse_pos

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_y -= camera_speed  # Move camera forward (W key)
    if keys[pygame.K_s]:
        camera_y += camera_speed  # Move camera backward (S key)
    if keys[pygame.K_a]:
        camera_x += camera_speed  # Move camera left (A key)
    if keys[pygame.K_d]:
        camera_x -= camera_speed  # Move the camera right (D key)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()  # Exit on Escape key press
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                zoom += zoom_speed
            elif event.button == 5:  # Mouse wheel down
                zoom -= zoom_speed
            elif event.button == 1:  # Left mouse button
                mouse_pressed = True
                last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                mouse_pressed = False
                # Get the 3D coordinates of the mouse cursor when clicked
                mouse_x, mouse_y, mouse_z = get_3d_coordinates()
                print(f"X={mouse_x:.3f}, Y={mouse_y:.3f}, Z={mouse_z:.3f}")
        elif event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                new_mouse_pos = pygame.mouse.get_pos()
                dx, dy = new_mouse_pos[0] - last_mouse_pos[0], new_mouse_pos[1] - last_mouse_pos[1]
                camera_rotation_x += dy * 0.3  # Adjust sensitivity for rotation
                camera_rotation_y += dx * 0.3
                last_mouse_pos = new_mouse_pos

    return zoom


# Main function
def main():
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (800, 600)

    # Create a Pygame window
    pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

    # Initialize OpenGL
    settings.init_opengl(window_size)

    # Set initial camera parameters
    initial_camera_position = (-1.8, -11, -10)
    zoom = -2
    zoom_speed = 0.15  # Define zoom_speed here

    while True:
        # Handle user input
        zoom = handle_input(zoom, zoom_speed)

        # Clear the screen
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply transformations
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(initial_camera_position[0] + camera_x,
                     initial_camera_position[1] + camera_y,
                     initial_camera_position[2] + zoom)
        glRotatef(camera_rotation_x, 1, 0, 0)  # Rotate based on mouse movement
        glRotatef(camera_rotation_y, 0, 1, 0)

        glPushMatrix()
        glColor3f(1,1,1)
        glScalef(2.2, 2.2, 2.2)
        glTranslatef(-4,2,0)
        texture.render_image("resources/texture_image.png")
        glPopMatrix()

        # Rendering functions for lower, upper body, head
        lower_body.render_lower_body()
        upper_body.render_upper_body()
        head.render_head()

        # Swap the display buffers
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
