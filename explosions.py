import random
import entityid, manager

big_explosions = [
    ('explosion_1.png', 10),
    ('explosion_2.png', 10),
    ('explosion_3.png', 7),
]

small_explosions = [
    ('explosion_small_1.png', 8),
    ('explosion_small_2.png', 7),
    ('explosion_small_3.png', 9),
]

explosion_entity = {
    'render': {
        'image_name': "explosion_1.png",
        'frames': 10,
        'layer': 2,
        'duration': 0.05,
    },
    'spatial': {
        'position': (128, 120),
        'angle': 0,
    },
    'animation_ai': None,
}

def create(at, big=True):
    entity_id = entityid.create()
    image, frames = random.choice(big_explosions if big else small_explosions)
    render = explosion_entity['render']
    render['image_name'] = image
    render['frames'] = frames
    explosion_entity['spatial']['position'] = at
    manager.create_entity(entity_id, explosion_entity)
    return entity_id
