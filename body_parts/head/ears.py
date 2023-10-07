from OpenGL.GL import *

from shapes import torus, cylinder, prisim, hemisphere

brown = (160 / 255.0, 90 / 255.0, 45 / 255.0)
red = (251 / 255.0, 75 / 255.0, 44 / 255.0)
grey = (160 / 255.0, 159 / 255.0, 163 / 255.0)


def render_left_ears():
    glPushMatrix()
    glTranslatef(3.3, 10, 0.5)
    glScalef(1, 1, 1)
    glRotatef(0, 0, 0, 0)
    torus.render_two_thirds_torus(red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.530, 11.67, 0.505)
    glScalef(1, 1, 1)
    glRotatef(-53, 0, 0, 1)
    cylinder.render_cylinder(0.28, 2.7, 20, red, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.5, 11.1, 0.505)
    glScalef(1, 1, 1)
    glRotatef(-1, 0, 0, 1)
    cylinder.render_cylinder(0.28, 2.7, 20, red, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.48, 12.34, 0.505)
    glScalef(2, 2.5, 1.83)
    glRotatef(90, 1, 0, -0.3)  # Rotate along z
    hemisphere.render_hemisphere(0.175, 20, 10, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.3, 10., 0.505)
    glScalef(0.95, 1.08, 0.5)
    glRotatef(90, 1, 0, 0)
    prisim.render_rectangular_prism(brown, False)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.78, 11.28, 0.505)
    glScalef(0.5, 0.5, 0.5)
    glRotatef(90, 1, 0, 0)
    # glRotatef(20, 0, 1, 0)
    prisim.render_rectangular_prism(brown, False)
    glPopMatrix()


def render_right_ears():
    glPushMatrix()
    glTranslatef(3, 10, 0.5)
    glScalef(1, 1, 1)
    glRotatef(0, 0, 0, 0)
    torus.render_two_thirds_torus(red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.230, 11.67, 0.505)
    glScalef(1, 1, 1)
    glRotatef(-53, 0, 0, 1)
    cylinder.render_cylinder(0.28, 2.7, 20, red, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.2, 11.1, 0.505)
    glScalef(1, 1, 1)
    glRotatef(-1, 0, 0, 1)
    cylinder.render_cylinder(0.28, 2.7, 20, red, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.18, 12.34, 0.505)
    glScalef(2, 2.5, 1.83)
    glRotatef(90, 1, 0, -0.3)  # Rotate along z
    hemisphere.render_hemisphere(0.175, 20, 10, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3., 10., 0.505)
    glScalef(0.95, 1.08, 0.5)
    glRotatef(90, 1, 0, 0)
    prisim.render_rectangular_prism(brown, False)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3.48, 11.28, 0.505)
    glScalef(0.5, 0.5, 0.5)
    glRotatef(90, 1, 0, 0)
    # glRotatef(20, 0, 1, 0)
    prisim.render_rectangular_prism(brown, False)
    glPopMatrix()


def draw_ears():
    glPushMatrix()
    glTranslatef(-0.265, 16.797, -0.327)
    glRotatef(-45, 0, 0, 1)
    glScalef(0.5, 1, 0.5)
    cylinder.render_cylinder(0.175, 1, 30, grey, grey, grey, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.665, 16.797, -0.327)
    glRotatef(45, 0, 0, 1)
    glScalef(0.5, 1, 0.5)
    cylinder.render_cylinder(0.175, 1, 30, grey, grey, grey, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.065, 12.597, -0.627)
    glScalef(0.5, 0.5, 0.5)
    render_right_ears()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.123, 13.65, -0.627)
    glRotatef(60, 0, 0, 1)
    glScalef(0.5, 0.5, 0.5)
    render_left_ears()
    glPopMatrix()
