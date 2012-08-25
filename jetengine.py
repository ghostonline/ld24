import planar, spatial

jetengines = {}
moving_ids = {}

def add_component(entity_id, speed):
    assert entity_id not in jetengines
    jetengines[entity_id] = float(speed)

def move(entity_id, direction):
    direction_vec = planar.Vec2(direction[0], direction[1])
    current = moving_ids.get(entity_id, planar.Vec2(0,0))
    moving_ids[entity_id] = current + direction_vec

def update(dt):
    global moving_ids
    for entity_id, direction in moving_ids.iteritems():
        speed = jetengines[entity_id] * dt
        speed_vec = direction.normalized() * speed
        spatial.move_vec(entity_id, speed_vec)
    moving_ids = {}
