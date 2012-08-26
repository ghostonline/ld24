import bullet, spatial

BULLET_IMAGE = 'cannon_fire.png'
BULLET_SPEED = 500

def dual_cannon(entity_id, state):
    offset = state.offset
    player_only = state.player_only
    pos_x, pos_y, angle = spatial.get_position_and_angle(entity_id)
    bullet.create((pos_x + offset, pos_y), angle, BULLET_SPEED,
                  BULLET_IMAGE, entity_id, player_only=player_only)
    bullet.create((pos_x - offset, pos_y), angle, BULLET_SPEED,
                  BULLET_IMAGE, entity_id, player_only=player_only)

def spreader_cannon(entity_id, state):
    offset = state.offset
    player_only = state.player_only
    pos_x, pos_y, angle = spatial.get_position_and_angle(entity_id)
    bullet.create((pos_x, pos_y), angle, BULLET_SPEED,
                  BULLET_IMAGE, entity_id, player_only=player_only)
    bullet.create((pos_x, pos_y), angle - offset, BULLET_SPEED,
                  BULLET_IMAGE, entity_id, player_only=player_only)
    bullet.create((pos_x, pos_y), angle + offset, BULLET_SPEED,
                  BULLET_IMAGE, entity_id, player_only=player_only)

DUAL, SPREADER = dual_cannon, spreader_cannon

cannons = {}

class CannonState:
    def __init__(self, trigger, hot, cooldown, offset, player_only, shoot_func):
        self.trigger = trigger
        self.hot = hot
        self.cooldown = cooldown
        self.offset = offset
        self.player_only = player_only
        self.shoot_func = shoot_func

def add_component(entity_id, cooldown, offset=8, player_only=False, type_=DUAL):
    assert entity_id not in cannons
    cannons[entity_id] = CannonState(False, 0, cooldown, offset, player_only,
                                     type_)

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
            state.shoot_func(entity_id, state)
        state.hot = hot
        state.trigger = False

