from OpenGL.GL import *
from shapes import cylinder, sphere

red = (251 / 255.0, 75 / 255.0, 44 / 255.0)
grey = (160 / 255.0, 159 / 255.0, 163 / 255.0)


def render_upper_left_arm():
    glPushMatrix()
    glTranslatef(-5, 11.6, -0.396)
    glRotatef(-30, 0, 0, 1)
    cylinder.render_cylinder(0.5, 2.9, 30, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-4.4, 13.1, -0.42)
    glScalef(0.2, 0.2, 0.2)
    sphere.render_sphere(2.2, 30, 30, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-3.9, 12.89, -0.4)
    glRotatef(90, 0, 0, 1)
    cylinder.render_cylinder(0.175, 1, 30, grey, grey, grey)
    glPopMatrix()


def render_upper_right_arm():
    glPushMatrix()
    glTranslatef(2.07, 11.6, -0.396)
    glRotatef(30, 0, 0, 1)
    cylinder.render_cylinder(0.5, 2.9, 30, red, red, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.45, 13.1, -0.42)
    glScalef(0.2, 0.2, 0.2)
    sphere.render_sphere(2.2, 30, 30, red)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.9, 12.89, -0.4)
    glRotatef(90, 0, 0, 1)
    cylinder.render_cylinder(0.175, 1, 30, grey, grey, grey)
    glPopMatrix()
