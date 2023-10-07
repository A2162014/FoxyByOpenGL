from OpenGL.GL import *
from shapes import prisim

grey = (167 / 255.0, 169 / 255.0, 173 / 255.0)


def render_palm():
    glPushMatrix()
    glTranslatef(2.78, 6.6, -0.19)
    glScalef(1, 0.476, 0.4)
    glRotatef(90, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_thumb():
    # Render the thumb – proximal (closest from palm)
    glPushMatrix()
    glTranslatef(2.74, 6.82, 0.2)
    glScalef(0.79, 0.29, 0.12)
    glRotatef(-104, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the thumb – middle
    glPushMatrix()
    glTranslatef(2.52, 6.4, 0.2)
    glScalef(0.68, 0.22, 0.12)
    glRotatef(-97, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the thumb – distal (farthest from the palm)
    glPushMatrix()
    glTranslatef(2.42, 6.0, 0.2)
    glScalef(0.62, 0.18, 0.12)
    glRotatef(-92, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_index_finger():
    # Render the index finger – proximal
    glPushMatrix()
    glTranslatef(2.98, 5.92, 0.095)
    glScalef(0.79, 0.29, 0.11)
    glRotatef(-95, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the index finger – the middle
    glPushMatrix()
    glTranslatef(2.82, 5.50, 0.095)
    glScalef(0.68, 0.22, 0.11)
    glRotatef(-101, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the index finger - distal
    glPushMatrix()
    glTranslatef(2.52, 5.12, 0.095)
    glScalef(0.56, 0.18, 0.11)
    glRotatef(-105, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_middle_finger():
    # Render the middle finger – proximal
    glPushMatrix()
    glTranslatef(2.98, 5.92, -0.189)
    glScalef(0.79, 0.29, 0.11)
    glRotatef(-95, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the middle finger – middle
    glPushMatrix()
    glTranslatef(2.82, 5.50, -0.189)
    glScalef(0.68, 0.22, 0.11)
    glRotatef(-101, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the middle finger – distal
    glPushMatrix()
    glTranslatef(2.52, 5.12, -0.189)
    glScalef(0.56, 0.18, 0.11)
    glRotatef(-105, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_ring_finger():
    # Render the ring finger – proximal
    glPushMatrix()
    glTranslatef(2.98, 5.92, -0.474)
    glScalef(0.79, 0.29, 0.11)
    glRotatef(-95, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the ring finger – middle
    glPushMatrix()
    glTranslatef(2.82, 5.50, -0.474)
    glScalef(0.68, 0.22, 0.11)
    glRotatef(-101, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()

    # Render the ring finger – distal
    glPushMatrix()
    glTranslatef(2.52, 5.12, -0.474)
    glScalef(0.56, 0.18, 0.11)
    glRotatef(-105, 0, 0, 1)
    prisim.render_rectangular_prism(grey)
    glPopMatrix()


def render_hand():
    render_palm()
    render_thumb()
    render_index_finger()
    render_middle_finger()
    render_ring_finger()
