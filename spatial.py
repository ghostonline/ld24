import planar

spatials = {}

def add_component(entity_id, position):
    assert entity_id not in spatials

    vec_pos = planar.Vec2(position[0], position[1])
    spatials[entity_id] = vec_pos

def get_position(entity_id):
    pos = spatials[entity_id]
    return (pos.x, pos.y)
