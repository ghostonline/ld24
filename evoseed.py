import health, spatial, collider, manager, explosions

DEFAULT_COLLECTOR_THRESHOLD = 100
DRIFT_SPEED = 50
EXPLODE_INTERVAL = 0.5
EXPLODE_RADIUS = 16

evoseeds = {}

collector_id = None
collected = 0
collected_change = False
collect_events = []

class State:
    def __init__(self, max_health, explode_timeout, radius):
        self.max_health = max_health
        self.explode_timeout = explode_timeout
        self.timeout = 0
        self.radius = radius

def add_component(entity_id, max_health):
    evoseeds[entity_id] = State(max_health, EXPLODE_INTERVAL, EXPLODE_RADIUS)

def remove_component(entity_id):
    del evoseeds[entity_id]

def update(dt):
    global collected, collected_change
    for entity_id, state in evoseeds.iteritems():
        max_health = state.max_health
        current_health = health.get_health(entity_id)
        if current_health > max_health:
            continue

        position = spatial.get_position_vec(entity_id)
        timeout = state.timeout - dt
        if timeout < 0:
            explosions.create_within_radius(position, state.radius, big=False)
            timeout = state.explode_timeout
        state.timeout = timeout

        nearest_collector, collector_position, collector_distance = spatial.nearest(
            entity_id, [collector_id], threshold=DEFAULT_COLLECTOR_THRESHOLD)
        if nearest_collector:
            pull_strength = 1 - collector_distance / DEFAULT_COLLECTOR_THRESHOLD
            drift_direction = (collector_position - position).normalized()
            drift = drift_direction * pull_strength * DRIFT_SPEED * dt
            spatial.move_vec(entity_id, drift)

    for entity_id, recipient_id in collect_events:
        addition = health.get_health(entity_id)
        health.heal(recipient_id, addition)
        collected += 1
        collected_change = True
        manager.destroy_entity(entity_id)

def process_events():
    global collect_events
    collect_events = []

    seed_ids = collider.collide_events.intersection(evoseeds)
    for seed_id in seed_ids:
        collide_ids = collider.collide_events_data[seed_id]
        if collector_id in collide_ids:
            current_health = health.get_health(seed_id)
            max_health = evoseeds[seed_id].max_health
            if current_health > max_health:
                continue
            collect_events.append((seed_id, collector_id))
