import pyglet
import spatial

window = None
renderables = {}
images = {}
sprite_batch = pyglet.graphics.Batch()

class SpriteState:
    def __init__(self, sprite, offset):
        self.sprite = sprite
        self.offset = offset

def add_component(entity_id, image_name):
    assert entity_id not in renderables

    try:
        image_res = images[image_name]
    except KeyError:
        image_res = pyglet.resource.image(image_name)
    images[image_name] = image_res

    sprite = pyglet.sprite.Sprite(image_res, batch=sprite_batch)
    offset = image_res.width * 0.5, image_res.height * 0.5
    renderables[entity_id] = SpriteState(sprite, offset)

def remove_component(entity_id):
    del renderables[entity_id]

def set_rotation(entity_id, angle):
    sprite = renderables[entity_id]
    sprite.rotation = angle

def update():
    for entity_id, state in renderables.iteritems():
        x, y = spatial.get_position(entity_id)
        offset = state.offset
        x -= offset[0]
        y -= offset[0]
        sprite = state.sprite
        sprite.x = x
        sprite.y = y

def draw():
    window.clear()
    sprite_batch.draw()
