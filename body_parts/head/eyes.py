from OpenGL.GL import *

from utilities.shapes import torus, hemisphere

brown = (160 / 255.0, 90 / 255.0, 45 / 255.0)
dark_red = (156 / 255.0, 54 / 255.0, 42 / 255.0)
outer_yellow = (238 / 255.0, 160 / 255.0, 0 / 255.0)
inner_yellow = (241 / 255.0, 195 / 255.0, 98 / 255.0)
white = (1, 1, 1)
black = (0, 0, 0)


def render_left_eye():
    # eye-brow
    glPushMatrix()
    glTranslatef(-2.023, 16.310, 0.824)
    glScalef(0.3, 0.2, 0.25)
    glRotatef(45, 0, 0, 1)
    torus.render_one_fourth_torus(dark_red, 1.1)
    glPopMatrix()

    # eye-patch + right eye connector
    glPushMatrix()
    glTranslatef(-1.54, 15.77, 0.96)
    glScalef(0.4, 0.25, 0.25)
    glRotatef(50, 0, 0, 1)
    # glRotatef(45, 0, 0, 1)
    torus.render_one_fourth_torus(black, 1.1)
    glPopMatrix()

    # eye-patch
    glPushMatrix()
    glTranslatef(-2.08, 15.9, 0.8)
    glScalef(0.25, 0.25, 0.25)
    glRotatef(180, 1, 0, 0)
    hemisphere.render_hemisphere(1.35, 20, 10, black)
    glPopMatrix()

    # eye-patch side
    glPushMatrix()
    glTranslatef(-2.2, 15.85, -0.1)
    glScalef(0.4, 0.4, 0.4)
    glRotatef(-90, 1, 0, 0)
    # glRotatef(-90, 0, 0, 1)
    torus.render_two_thirds_torus(black, 2, 0.3)
    glPopMatrix()


def render_right_eye():
    # eye-brow
    glPushMatrix()
    glTranslatef(-1.1, 16.310, 0.824)
    glScalef(0.3, 0.2, 0.25)
    glRotatef(45, 0, 0, 1)
    torus.render_one_fourth_torus(dark_red, 1.1)
    glPopMatrix()

    # eyeball
    glPushMatrix()
    glTranslatef(-1, 15.9, 0.8)
    glScalef(0.25, 0.25, 0.25)
    glRotatef(180, 1, 0, 0)
    hemisphere.render_hemisphere(1.35, 20, 10, white)
    glPopMatrix()

    # iris
    glPushMatrix()
    glTranslatef(-1.020, 15.901, 1.109)
    glScalef(1.4, 1.4, 1.34)
    glRotatef(180, 1, 0, 0)
    hemisphere.render_hemisphere(0.08, 20, 10, outer_yellow)
    glPopMatrix()

    # pupil
    glPushMatrix()
    glTranslatef(-1.020, 15.901, 1.15)
    glScalef(0.92, 0.92, 0.92)
    glRotatef(180, 1, 0, 0)
    hemisphere.render_hemisphere(0.08, 20, 10, inner_yellow)
    glPopMatrix()

    # eyelid
    glPushMatrix()
    glTranslatef(-1, 15.9, 0.8)
    glScalef(0.27, 0.27, 0.27)
    glRotatef(60, 1, 0, 0)
    hemisphere.render_hemisphere(1.35, 20, 10, dark_red)
    glPopMatrix()
