pressed_keys = []

def on_up(key, x, y):
    if key in pressed_keys:
        pressed_keys.remove(key)

def on_down(key, x, y):
    if key not in pressed_keys:
        pressed_keys.append(key)

def is_key_pressed(key):
    return key in pressed_keys
