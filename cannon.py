import spatial, render, entityid

BULLET_IMAGE = 'cannon_fire.png'

cannons = {}

class CannonState:
    def __init__(self, trigger, hot, cooldown):
        self.trigger = trigger
        self.hot = hot
        self.cooldown = cooldown

def add_component(entity_id, cooldown):
    assert entity_id not in cannons
    cannons[entity_id] = CannonState(False, 0, cooldown)

def fire(entity_id):
    cannons[entity_id].trigger = True

def update(dt):
    for entity_id, state in cannons.iteritems():
        hot = state.hot
        if hot:
            hot -= min(hot, dt)
        if state.trigger and not hot:
            hot = state.cooldown
            _create_bullet(entity_id)
        state.hot = hot
        state.trigger = False

def _create_bullet(entity_id):
    pos = spatial.get_position(entity_id)
    bullet_id = entityid.create()
    spatial.add_component(bullet_id, pos)
    render.add_component(bullet_id, BULLET_IMAGE)
