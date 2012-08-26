import missile_ai, bullet_ai, health, manager, trigger, score, explosions, spatial

enemies = set()
press_trigger = []

MISSILE_DAMAGE_MULT = 4

def add_component(entity_id):
    assert entity_id not in enemies
    enemies.add(entity_id)
    press_trigger.append(entity_id)

def remove_component(entity_id):
    enemies.remove(entity_id)
    try:
        press_trigger.remove(entity_id)
    except ValueError:
        pass

def update(dt):
    damaged = enemies.intersection(bullet_ai.hit)
    for entity_id in damaged:
        damage = bullet_ai.hit_data[entity_id]
        health.apply_damage(entity_id, damage)

    damaged = enemies.intersection(missile_ai.hit)
    for entity_id in damaged:
        damage = missile_ai.hit_data[entity_id]
        health.apply_damage(entity_id, damage * MISSILE_DAMAGE_MULT)
    
    global press_trigger
    for entity_id in press_trigger:
        trigger.hold(entity_id)
    press_trigger = []

def process_events():
    dead_enemies = enemies.intersection(health.killed)
    for entity_id in dead_enemies:
        score.award(entity_id)
        position = spatial.get_position(entity_id)
        explosions.create(position)
        manager.destroy_entity(entity_id)
