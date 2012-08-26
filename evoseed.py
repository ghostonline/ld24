import health, spatial, collider, manager

DEFAULT_COLLECTOR_THRESHOLD = 100
DRIFT_SPEED = 50

evoseeds = {}

collector_id = None
collect_events = []

def add_component(entity_id, max_health):
    evoseeds[entity_id] = max_health

def remove_component(entity_id):
    del evoseeds[entity_id]

def update(dt):
    for entity_id, max_health in evoseeds.iteritems():
        current_health = health.get_health(entity_id)
        if current_health > max_health:
            continue
        nearest_collector, collector_position, collector_distance = spatial.nearest(
            entity_id, [collector_id], threshold=DEFAULT_COLLECTOR_THRESHOLD)
        if nearest_collector:
            position = spatial.get_position_vec(entity_id)
            pull_strength = 1 - collector_distance / DEFAULT_COLLECTOR_THRESHOLD
            drift_direction = (collector_position - position).normalized()
            drift = drift_direction * pull_strength * DRIFT_SPEED * dt
            spatial.move_vec(entity_id, drift)

    for entity_id, recipient_id in collect_events:
        addition = health.get_health(entity_id)
        health.heal(recipient_id, addition)
        manager.destroy_entity(entity_id)

def process_events():
    global collect_events
    collect_events = []

    seed_ids = collider.collide_events.intersection(evoseeds)
    for seed_id in seed_ids:
        collide_ids = collider.collide_events_data[seed_id]
        if collector_id in collide_ids:
            current_health = health.get_health(seed_id)
            max_health = evoseeds[seed_id]
            if current_health > max_health:
                continue
            collect_events.append((seed_id, collector_id))
