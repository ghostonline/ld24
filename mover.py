import spatial

movers = {}

class State:
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed
        self.target = None

def add_component(entity_id, distance, speed):
    movers[entity_id] = State(distance, speed)

def remove_component(entity_id):
    del movers[entity_id]

def update(dt):
    for entity_id, state in movers.iteritems():
        position = spatial.get_position(entity_id)
        if not state.target:
            state.target = position[1] - state.distance
        position_y = position[1] - state.speed * dt
        if position_y < state.target:
           position_y += state.distance
        spatial.set_position_and_angle(entity_id, (position[0], position_y), 0)
