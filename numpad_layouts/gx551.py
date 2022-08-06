from libevdev import EV_KEY

# Subtract 0.3 (a third key) as the UX581L has about a third key space at the top
top_offset = 0

touchpad_physical_buttons_are_inside_numpad = False

top_right_icon_width = 400
top_right_icon_height = 400
top_right_icon_is_on_top_left = True

keys = [
    [None, EV_KEY.KEY_KPSLASH, EV_KEY.KEY_KPASTERISK, EV_KEY.KEY_KPMINUS],
    [EV_KEY.KEY_KP7, EV_KEY.KEY_KP8, EV_KEY.KEY_KP9, EV_KEY.KEY_KPPLUS],
    [EV_KEY.KEY_KP4, EV_KEY.KEY_KP5, EV_KEY.KEY_KP6, EV_KEY.KEY_KPPLUS],
    [EV_KEY.KEY_KP1, EV_KEY.KEY_KP2, EV_KEY.KEY_KP3, EV_KEY.KEY_KPENTER],
    [EV_KEY.KEY_KP0, EV_KEY.KEY_KP0, EV_KEY.KEY_KPDOT, EV_KEY.KEY_KPENTER]
]
