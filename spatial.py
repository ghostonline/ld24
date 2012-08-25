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

def get_position_and_angle(entity_id):
    state = spatials[entity_id]
    pos = state.position
    angle = state.angle
    return (pos.x, pos.y, angle)

def get_position_vec(entity_id):
    return spatials[entity_id].position

def move_vec(entity_id, delta_vec):
    state = spatials[entity_id]
    state.position = state.position + delta_vec

def move_forward(entity_id, distance):
    state = spatials[entity_id]
    state.position = state.position + state.trajectory * distance

def nearest(origin_id, group, threshold):
    origin_pos = spatials[origin_id].position

    relevant = [(id_, spatials[id_].position) for id_ in group]
    nearest_id, nearest_position = relevant.pop()
    nearest_distance = origin_pos.distance_to(nearest_position)

    for entity_id, position in relevant:
        distance = origin_pos.distance_to(position)
        if distance < nearest_distance:
            nearest_id = entity_id
            nearest_position = position

    if nearest_distance < threshold:
        result = nearest_id, nearest_position, nearest_distance
    else:
        result = (None, None, None)
    return result
