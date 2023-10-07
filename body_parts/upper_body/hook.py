from OpenGL.GL import *
from shapes import cylinder, torus, cone

grey = (167 / 255.0, 169 / 255.0, 173 / 255.0)


def render_holder():
    glPushMatrix()
    glTranslatef(-6.324, 7.55, 1.24)
    glRotatef(-45, 1, 1, 0)
    cylinder.render_cylinder(0.4, 0.3, 30, grey, grey, grey)
    glPopMatrix()


def render_hook_connector():
    glPushMatrix()
    glTranslatef(-7.0, 7.5, 1.3)
    glScalef(0.6, 0.6, 0.6)
    glRotatef(140, 1, 0, 0)
    torus.render_one_fourth_torus(grey, 1.1, 0.19)
    glPopMatrix()


def render_hook_body():
    glPushMatrix()
    glTranslatef(-6.4, 6.6, 2)
    glScalef(0.6, 0.6, 0.6)
    glRotatef(-35, 1, 0, 0)
    torus.render_two_thirds_torus(grey, 1.1, 0.17)
    glPopMatrix()


def render_tip():
    glPushMatrix()
    glTranslatef(-5.74, 6.617, 2.02)
    glScalef(0.55, 0.55, 0.55)
    glRotatef(-120, 1, 0, 0)
    cone.render_cone(grey, 0.24, 1)
    glPopMatrix()


def render_hook():
    render_holder()
    render_hook_connector()
    render_hook_body()
    render_tip()
