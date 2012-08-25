import pyglet
import spatial

window = None
renderables = {}
images = {}
sprite_batch = pyglet.graphics.Batch()

def add_component(entity_id, image_name):
    assert entity_id not in renderables

    try:
        image_res = images[image_name]
    except KeyError:
        image_res = pyglet.resource.image(image_name)
    images[image_name] = image_res

    sprite = pyglet.sprite.Sprite(image_res, batch=sprite_batch)
    renderables[entity_id] = sprite

def update():
    for entity_id, sprite in renderables.iteritems():
        sprite.x, sprite.y = spatial.get_position(entity_id)

def draw():
    window.clear()
    sprite_batch.draw()
