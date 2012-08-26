import health

forcefields = {}

class State:
    def __init__(self, timeout, active):
        self.timeout = timeout
        self.active = active

def add_component(entity_id, timeout):
    assert entity_id not in forcefields
    forcefields[entity_id] = State(timeout, False)

def remove_component(entity_id):
    try:
        state = forcefields[entity_id]
        if state.active:
            health.set_vurnable(entity_id, True)
    finally:
        del forcefields[entity_id]

def update(dt):
    stop_me = []
    for entity_id, state in forcefields.iteritems():
        timeout, active = state.timeout, state.active
        timeout -= dt
        if timeout > 0:
            if not active:
                health.set_vurnable(entity_id, False)
                state.active = True
        else:
            stop_me.append(entity_id)
        state.timeout = timeout

    for entity_id in stop_me:
        remove_component(entity_id)
