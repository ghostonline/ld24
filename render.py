import pyglet
import planar
import spatial

window = None
renderables = {}
images = {}
images_atlas = {}

def texture_set_filter_nearest( texture ):
    pyglet.gl.glBindTexture( texture.target, texture.id )
    pyglet.gl.glTexParameteri( texture.target, pyglet.gl.GL_TEXTURE_MAG_FILTER,
                              pyglet.gl.GL_NEAREST )
    pyglet.gl.glTexParameteri( texture.target, pyglet.gl.GL_TEXTURE_MIN_FILTER,
                              pyglet.gl.GL_NEAREST )
    pyglet.gl.glBindTexture( texture.target, 0 )

class ScaleGroup(pyglet.graphics.Group):
    def set_state(self):
        pyglet.gl.glPushMatrix()
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glScalef(2.0, 2.0, 1.0)

    def unset_state(self):
        pyglet.gl.glPopMatrix()

sprite_batch = pyglet.graphics.Batch()
sprite_group = ScaleGroup()
sprite_layers = {}

class SpriteState:
    def __init__(self, sprite, offset, atlas):
        self.sprite = sprite
        self.offset = offset
        self.atlas = atlas

def add_component(entity_id, image_name, frames=1, loop=False, duration=0,
                  autoplay=True,select=1, layer=0):
    assert entity_id not in renderables

    try:
        image_res = images[image_name]
    except KeyError:
        image_res = pyglet.resource.image(image_name)
        texture_set_filter_nearest(image_res.get_texture())
    images[image_name] = image_res

    try:
        atlas, texture = images_atlas[image_name]
    except KeyError:
        atlas = pyglet.image.ImageGrid(image_res, 1, frames)
        texture = pyglet.image.TextureGrid(atlas)
    images_atlas[image_name] = atlas, texture

    if frames > 1 and autoplay:
        sprite_res = pyglet.image.Animation.from_image_sequence(
                                            texture[:frames], duration, loop)
    elif frames > 1:
        sprite_res = texture[select]
    else:
        sprite_res = image_res

    layer_num = int(layer)
    try:
        layer_group = sprite_layers[layer_num]
    except KeyError:
        layer_group = pyglet.graphics.OrderedGroup(layer_num, parent=sprite_group)
    sprite_layers[layer_num] = layer_group

    sprite = pyglet.sprite.Sprite(sprite_res, batch=sprite_batch,
                                  group=layer_group)
    offset = planar.Vec2(image_res.width * 0.5 / frames, image_res.height * 0.5)
    renderables[entity_id] = SpriteState(sprite, offset, atlas)

def remove_component(entity_id):
    sprite_state = renderables[entity_id]
    sprite_state.sprite.batch = None
    sprite_state.sprite.group = None
    del renderables[entity_id]

def set_rotation(entity_id, angle):
    sprite = renderables[entity_id]
    #TODO: Check this ---v
    sprite.rotation = angle

def set_frame(entity_id, framenum):
    state = renderables[entity_id]
    state.sprite.image = state.atlas[framenum]

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
