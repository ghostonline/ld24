import bullet_ai, health, manager, cannon

enemies = set()

def add_component(entity_id):
    assert entity_id not in enemies
    enemies.add(entity_id)

def remove_component(entity_id):
    enemies.remove(entity_id)

def update(dt):
    damaged = enemies.intersection(bullet_ai.hit)
    for entity_id in damaged:
        damage = bullet_ai.hit_data[entity_id]
        health.apply_damage(entity_id, damage)
    
    for entity_id in enemies:
        cannon.fire(entity_id)

def process_events():
    dead_enemies = enemies.intersection(health.killed)
    for entity_id in dead_enemies:
        manager.destroy_entity(entity_id)
