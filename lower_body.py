from OpenGL.GL import *
from body_parts.lower_body import feet, lower_leg, upper_leg, groin


def render_leg():
    upper_leg.render_upper_leg()
    lower_leg.render_lower_leg()


def render_lower_body():
    groin.render_groin()
    render_leg()
    feet.render_feet()
    glTranslatef(3, 0, 0)
    render_leg()
    feet.render_feet()
