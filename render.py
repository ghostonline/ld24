import pyglet
import planar
import spatial

window = None
renderables = {}
images = {}
images_atlas = {}

sprite_batch = pyglet.graphics.Batch()

class SpriteState:
    def __init__(self, sprite, offset):
        self.sprite = sprite
        self.offset = offset

def add_component(entity_id, image_name, frames=1, loop=False, duration=0,
                  autoplay=True,select=1):
    assert entity_id not in renderables

    try:
        image_res = images[image_name]
    except KeyError:
        image_res = pyglet.resource.image(image_name)
    images[image_name] = image_res

    try:
        atlas = images_atlas[image_name]
    except KeyError:
        atlas = pyglet.image.ImageGrid(image_res, 1, frames)
    images_atlas[image_name] = atlas

    if frames > 1 and autoplay:
        sprite_res = pyglet.image.Animation.from_image_sequence(
                                            atlas[:frames], duration, loop)
    elif frames > 1:
        sprite_res = atlas[select]
    else:
        sprite_res = image_res

    sprite = pyglet.sprite.Sprite(sprite_res, batch=sprite_batch)
    offset = planar.Vec2(image_res.width * 0.5 / frames, image_res.height * 0.5)
    renderables[entity_id] = SpriteState(sprite, offset)

def remove_component(entity_id):
    sprite_state = renderables[entity_id]
    sprite_state.sprite.batch = None
    del renderables[entity_id]

def set_rotation(entity_id, angle):
    sprite = renderables[entity_id]
    sprite.rotation = angle

def update(dt):
    for entity_id, state in renderables.iteritems():
        x, y, angle = spatial.get_position_and_angle(entity_id)
        offset = state.offset.rotated(-angle)
        x -= offset.x
        y -= offset.y
        sprite = state.sprite
        sprite.x = x
        sprite.y = y
        sprite.rotation = angle

def draw():
    window.clear()
    sprite_batch.draw()
