from OpenGL.GL import *

from shapes import hemisphere, cone, sphere

red = (251 / 255.0, 76 / 255.0, 43 / 255.0)
peach = (245 / 255.0, 189 / 255.0, 173 / 255.0)

white = (1, 1, 1)
black = (0, 0, 0)


def render_snout():
    glPushMatrix()
    glTranslatef(-1.48, 15, 0.65)
    glScalef(0.7, 0.95, 2)
    glRotatef(90, 1, 0, 0)
    hemisphere.render_hemisphere(1, 20, 10, peach)
    glPopMatrix()


def render_upper_jaw():
    glPushMatrix()
    glTranslatef(-1.48, 15, 0.65)
    glScalef(0.7, 0.1, 2)
    glRotatef(-90, 1, 0, 0)
    hemisphere.render_hemisphere(1, 20, 10, black)
    glPopMatrix()


def render_nose():
    # Render Nose
    glPushMatrix()
    glTranslatef(-1.462, 15.42, 2.27)
    glScalef(0.3, 0.3, 0.3)
    glRotatef(45, 1, 0, 0)
    sphere.render_sphere(0.7, 20, 10, black)
    glPopMatrix()


def render_lower_jaw():
    glPushMatrix()
    glTranslatef(-1.48, 15.07, 0.57)
    glRotatef(55, -1, 0, 0)
    glScalef(0.75, 2.3, 0.1)
    hemisphere.render_hemisphere(0.97, 20, 10, black)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.48, 15.07, 0.57)
    glRotatef(55, -1, 0, 0)
    glScalef(0.75, 2.3, 1)
    hemisphere.render_hemisphere(0.97, 20, 10, red)
    glPopMatrix()


def render_teeth():
    glPushMatrix()
    glTranslatef(-2.059, 15, 0.790)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Upper Tooth -1 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.080, 15, 1.037)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Upper Tooth -2 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.034, 15, 1.27)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Upper Tooth -3 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.975, 15, 1.603)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.4, 6)  # Upper Tooth -4 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.864, 15, 1.916)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.4, 6.5)  # Upper Tooth -5 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.755, 15, 2.234)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.5, 6.5)  # Upper Tooth -6 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.479, 15, 2.492)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.5, 6.5)  # Upper Tooth -7 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.191, 15, 2.234)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.5, 6.5)  # Upper Tooth -8 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.055, 15, 1.916)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.4, 6.5)  # Upper Tooth -9 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.966, 15, 1.603)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.4, 6)  # Upper Tooth -10 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.887, 15, 1.27)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Upper Tooth -11 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.904, 15, 1.037)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Upper Tooth -12 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.860, 15, 0.790)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(90, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Upper Tooth -13 (from left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.039, 14.621, 1.122)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Lower Tooth -1 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.015, 14.481, 1.299)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Lower Tooth -2 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.989, 14.372, 1.503)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Lower Tooth -3 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.922, 14.225, 1.694)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Lower Tooth -4 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.848, 14.099, 1.878)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Lower Tooth -5 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.760, 13.983, 2.058)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-59, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 6)  # Lower Tooth -6 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.618, 13.869, 2.235)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-67, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 7)  # Lower Tooth -7 (from the left)
    glPopMatrix()
#right side
    glPushMatrix()
    glTranslatef(-1.337, 13.869, 2.235)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-67, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 7)  # Lower Tooth -8 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.234, 13.983, 2.058)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-59, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 6)  # Lower Tooth -9 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.139, 14.099, 1.878)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Lower Tooth -10 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.067, 14.225, 1.694)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 5)  # Lower Tooth -11 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.999, 14.372, 1.503)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Lower Tooth -12 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.977, 14.481, 1.299)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Lower Tooth -13 (from the left)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.885, 14.621, 1.122)
    glScalef(0.08, 0.08, 0.08)
    glRotatef(-55, 1.0, 0.0, 0.0)  # Rotate around the x-axis
    cone.render_cone(white, 1.3, 4)  # Upper Tooth -14 (from left)
    glPopMatrix()

def render_mouth():
    render_snout()
    render_upper_jaw()
    render_nose()
    render_lower_jaw()
    render_teeth()
