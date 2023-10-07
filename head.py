from body_parts.head import neck, base, mouth, eyes, ears


def render_head():
    neck.render_neck()
    base.render_base()
    mouth.render_mouth()
    eyes.render_left_eye()
    eyes.render_right_eye()
    ears.draw_ears()
