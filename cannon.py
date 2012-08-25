import bullet, spatial

BULLET_IMAGE = 'cannon_fire.png'
BULLET_SPEED = 1000

cannons = {}

class CannonState:
    def __init__(self, trigger, hot, cooldown):
        self.trigger = trigger
        self.hot = hot
        self.cooldown = cooldown

def add_component(entity_id, cooldown):
    assert entity_id not in cannons
    cannons[entity_id] = CannonState(False, 0, cooldown)

def remove_component(entity_id):
    del cannons[entity_id]

def fire(entity_id):
    cannons[entity_id].trigger = True

def update(dt):
    for entity_id, state in cannons.iteritems():
        hot = state.hot
        if hot:
            hot -= min(hot, dt)
        if state.trigger and not hot:
            hot = state.cooldown
            pos_x, pos_y, angle = spatial.get_position_and_angle(entity_id)
            bullet.create((pos_x, pos_y), angle, BULLET_SPEED, BULLET_IMAGE)
        state.hot = hot
        state.trigger = False

