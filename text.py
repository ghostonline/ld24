import pyglet
import spatial

FONT_NAME = 'visitor1.ttf'
FONT_FAMILY = 'Visitor TT1 BRK'

pyglet.resource.add_font(FONT_NAME)
game_font = pyglet.font.load(FONT_FAMILY)

texts = {}

def add_component(entity_id, text):
    assert entity_id not in texts
    texts[entity_id] = pyglet.text.Label(text, font_name=FONT_FAMILY)

def remove_component(entity_id):
    del texts[entity_id]

def update(dt):
    for entity_id, label in texts.iteritems():
        position = spatial.get_position(entity_id)
        label.x, label.y = int(position[0] * 2), int(position[1] * 2)

def set_text(entity_id, text):
    label = texts[entity_id]
    label.text = text

def draw():
    for label in texts.itervalues():
        label.draw()
