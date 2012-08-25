import planar, spatial, collider, bullet

bullets = {}
render_update = []

def add_component(entity_id, speed):
    assert entity_id not in bullets
    bullets[entity_id] = speed

def remove_component(entity_id):
    del bullets[entity_id]

def update(dt):
    for entity_id, speed in bullets.iteritems():
        distance =  speed * dt
        spatial.move_forward(entity_id, distance)

def process_events():
    bullet_ids = set(bullets)
    left_world = bullet_ids.intersection(collider.events)
    for entity_id in left_world:
        bullet.destroy(entity_id)
