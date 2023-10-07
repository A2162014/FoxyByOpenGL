from body_parts.upper_body import torso, lower_arm, upper_arm, hook, hand


def render_left_arm():
    lower_arm.render_lower_left_arm()
    upper_arm.render_upper_left_arm()


def render_right_arm():
    lower_arm.render_lower_right_arm()
    upper_arm.render_upper_right_arm()


def render_upper_body():
    torso.render_torso()
    render_left_arm()
    hook.render_hook()
    render_right_arm()
    hand.render_hand()
