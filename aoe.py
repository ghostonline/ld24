import manager
import collections
import collider

aoe_effects = {}

hit = {}

def add_component(entity_id, func, data):
    assert entity_id not in aoe_effects
    aoe_effects[entity_id] = (func, data)

def remove_component(entity_id):
    del aoe_effects[entity_id]

def update(dt):
    for entity_id, target_ids in hit.iteritems():
        func, data = aoe_effects[entity_id]
        func(target_ids, data)
        manager.destroy_entity(entity_id)

def process_events():
    aoe_ids = set(aoe_effects)

    global hit
    hit = {}
    struck_target = aoe_ids.intersection(collider.collide_events)
    for entity_id in struck_target:
        if entity_id not in aoe_effects:
            continue
        target_ids = collider.collide_events_data[entity_id]
        target_ids = [id_ for id_ in target_ids]
        hit[entity_id] = target_ids
