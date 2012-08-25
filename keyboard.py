from pyglet.window import key

keystate = None

UP, DOWN, LEFT, RIGHT = key.UP, key.DOWN, key.LEFT, key.RIGHT
FIRE = key.SPACE

def key_down(key_id):
    return keystate[key_id]
