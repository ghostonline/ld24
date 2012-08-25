import health, spatial

DEFAULT_COLLECTOR_THRESHOLD = 100
DRIFT_SPEED = 50

evoseeds = {}

collector_id = None

def add_component(entity_id, max_health):
    evoseeds[entity_id] = max_health

def remove_component(entity_id, max_health):
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
