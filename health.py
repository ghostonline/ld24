health = {}
damage_dealt = {}

killed = set()
damaged = set()

def add_component(entity_id, amount):
    assert entity_id not in health
    health[entity_id] = amount

def remove_component(entity_id):
    del health[entity_id]
    try:
        del damage_dealt[entity_id]
    except KeyError:
        pass

def update(dt):
    global damage_dealt, killed, damaged
    killed = set()
    damaged = set()
    for entity_id, damage in damage_dealt.iteritems():
        current_health = health[entity_id]
        current_health -= damage
        if current_health < 0:
            killed.add(entity_id)
        else:
            damaged.add(entity_id)
        health[entity_id] = current_health
    damage_dealt = {}

def apply_damage(entity_id, amount):
    damage = damage_dealt.get(entity_id, 0)
    damage += amount
    damage_dealt[entity_id] = damage

def get_health(entity_id):
    return health[entity_id]
