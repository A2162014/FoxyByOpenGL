from OpenGL.GL import *
from shapes import cylinder, hemisphere

red = (251 / 255.0, 75 / 255.0, 44 / 255.0)
grey = (160 / 255.0, 159 / 255.0, 163 / 255.0)


def render_lower_left_arm():
    glPushMatrix()
    glTranslatef(-6.1, 8.83, 0.48)
    glRotatef(-45, 1, 1, 0)
    cylinder.render_cylinder(0.4, 2.7, 30, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-5.796, 10.21, -0.33)
    glRotatef(-45, 1, 1, 0)
    cylinder.render_cylinder(0.175, 0.6, 30, grey, grey, grey)
    glPopMatrix()


def render_lower_right_arm():
    glPushMatrix()
    glTranslatef(2.9, 8.71, -0.29)
    glRotatef(-5, 1, -1, 0)
    cylinder.render_cylinder(0.4, 2.7, 30, red, red, red)
    glPopMatrix()

    # render joint between lower and upper arm
    glPushMatrix()
    glTranslatef(2.82, 10.2, -0.35)
    glRotatef(-5, 1, -1, 0)
    cylinder.render_cylinder(0.175, 1, 30, grey, grey, grey)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.89, 7.39, -0.187)
    glScalef(0.21, 0.21, 0.21)
    glRotatef(-90, 1, 0, 0)
    hemisphere.render_hemisphere(1.7, 30, 30, grey)
    glPopMatrix()
