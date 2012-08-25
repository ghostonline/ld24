import planar

spatials = {}

class State:
    def __init__(self, position, angle, trajectory):
        self.position = position
        self.angle = angle
        self.trajectory = trajectory

def add_component(entity_id, position, angle):
    assert entity_id not in spatials

    vec_pos = planar.Vec2(position[0], position[1])
    trajectory = planar.Vec2(0, 1).rotated(-angle)
    spatials[entity_id] = State(vec_pos, angle, trajectory)

def remove_component(entity_id):
    del spatials[entity_id]

def get_position(entity_id):
    pos = spatials[entity_id].position
    return (pos.x, pos.y)

def get_position_vec(entity_id):
    return spatials[entity_id].position

def move_vec(entity_id, delta_vec):
    state = spatials[entity_id]
    state.position = state.position + delta_vec

def move_forward(entity_id, distance):
    state = spatials[entity_id]
    state.position = state.position + state.trajectory * distance
