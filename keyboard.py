from pyglet.window import key

keystate = None

UP, DOWN, LEFT, RIGHT = key.UP, key.DOWN, key.LEFT, key.RIGHT
FIRE = key.Z

def key_down(key_id):
    return keystate[key_id]

def remove_component(entity_id):
    raise KeyError(entity_id)
