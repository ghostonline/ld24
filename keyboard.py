from pyglet.window import key

keystate = None

UP, DOWN, LEFT, RIGHT = key.UP, key.DOWN, key.LEFT, key.RIGHT

def key_down(key_id):
    return keystate[key_id]
