import planar, spatial, collider, manager
import collections

bullets = {}
render_update = []

hit = set()
hit_data = collections.Counter()

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
    left_world = bullet_ids.intersection(collider.world_events)
    for entity_id in left_world:
        manager.destroy_entity(entity_id)

    global hit, hit_data
    hit = set()
    hit_data = collections.Counter()
    struck_target = bullet_ids.intersection(collider.collide_events)
    for entity_id in struck_target:
        target_ids = collider.collide_events_data[entity_id]
        map(hit.add, target_ids)
        hit_data.update(target_ids)
        manager.destroy_entity(entity_id)
