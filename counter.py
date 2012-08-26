import collections
countables = {}
counters = collections.Counter()

def add_component(entity_id, cat='default'):
    assert entity_id not in countables
    counters.update([cat])
    countables[entity_id] = cat

def remove_component(entity_id):
    cat = countables[entity_id]
    del countables[entity_id]
    counters.subtract([cat])

def get_count(cat='default'):
    return counters[cat]
