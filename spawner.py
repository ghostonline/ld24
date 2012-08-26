import manager, entityid, spatial

spawners = {}

class State:
    def __init__(self, cooldown, entity_data):
        self.cooldown = cooldown
        self.entity_data = entity_data
        self.timeout = 0
        self.count = 0

def add_component(entity_id, cooldown, entity_data):
    assert entity_id not in spawners
    spawners[entity_id] = State(cooldown, entity_data)

def remove_component(entity_id):
    del spawners[entity_id]

def update(dt):
    for entity_id, state in spawners.iteritems():
        timeout = state.timeout
        timeout -= dt
        if timeout < 0:
            spawn_id = entityid.create()
            manager.create_entity(spawn_id, state.entity_data)
            spatial.copy_data(entity_id, spawn_id)
            state.count += 1
            timeout = state.cooldown
        state.timeout = timeout

def spawn_count(entity_id):
    state = spawners[entity_id]
    return state.count
