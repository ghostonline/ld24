triggers = {}

def add_component(entity_id):
    assert entity_id not in triggers
    triggers[entity_id] = False

def remove_component(entity_id):
    del triggers[entity_id]

def hold(entity_id):
    triggers[entity_id] = True

def release(entity_id):
    triggers[entity_id] = False

def is_down(entity_id):
    return triggers[entity_id]
