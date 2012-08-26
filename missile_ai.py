import planar, spatial, collider, manager, explosions
import collections

missiles = {}
render_update = []

hit = set()
hit_data = collections.Counter()

def add_component(entity_id, speed, owner):
    assert entity_id not in missiles
    missiles[entity_id] = (speed, owner)

def remove_component(entity_id):
    del missiles[entity_id]

def update(dt):
    for entity_id, data in missiles.iteritems():
        speed, owner = data
        distance =  speed * dt
        spatial.move_forward(entity_id, distance)

def process_events():
    missile_ids = set(missiles)
    left_world = missile_ids.intersection(collider.world_events)
    for entity_id in left_world:
        manager.destroy_entity(entity_id)

    global hit, hit_data
    hit = set()
    hit_data = collections.Counter()
    struck_target = missile_ids.intersection(collider.collide_events)
    for entity_id in struck_target:
        if entity_id not in missiles:
            continue
        target_ids = collider.collide_events_data[entity_id]
        owner_id = missiles[entity_id][1]
        target_ids = [id_ for id_ in target_ids if id_ != owner_id]
        if target_ids:
            map(hit.add, target_ids)
            hit_data.update(target_ids)
            position = spatial.get_position(entity_id)
            explosions.create(position, big=True)
            manager.destroy_entity(entity_id)
