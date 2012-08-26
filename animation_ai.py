import render, manager

animations = set()

def add_component(entity_id):
    assert entity_id not in animations
    animations.add(entity_id)

def remove_component(entity_id):
    animations.remove(entity_id)

def update(dt):
    finished = animations.intersection(render.finished)
    for entity_id in finished:
        manager.destroy_entity(entity_id)
