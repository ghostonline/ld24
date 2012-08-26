import bullet_ai, health, manager, cannon, score, explosions, spatial

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
        score.award(entity_id)
        position = spatial.get_position(entity_id)
        explosions.create(position)
        manager.destroy_entity(entity_id)
