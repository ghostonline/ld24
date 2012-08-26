import trigger, bullet, spatial

IMAGE = 'missile.png'
SPEED = 300

launchers = {}

class State:
    def __init__(self, hot, cooldown, offset, player_only):
        self.hot = hot
        self.cooldown = cooldown
        self.offset = offset
        self.player_only = player_only

def add_component(entity_id, cooldown, offset=8, player_only=False):
    assert entity_id not in launchers
    launchers[entity_id] = State(0, cooldown, offset, player_only)

def remove_component(entity_id):
    del launchers[entity_id]

def update(dt):
    for entity_id, state in launchers.iteritems():
        hot = state.hot
        if hot:
            hot -= min(hot, dt)
        elif trigger.is_down(entity_id):
            hot = state.cooldown
            offset = state.offset
            player_only = state.player_only
            pos_x, pos_y, angle = spatial.get_position_and_angle(entity_id)
            bullet.create_missile((pos_x + offset, pos_y), angle, SPEED, IMAGE,
                                  entity_id, player_only=player_only)
            state.offset = -offset
        state.hot = hot
        state.trigger = False

