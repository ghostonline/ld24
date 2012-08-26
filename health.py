health = {}
balance_change = {}

killed = set()
damaged = set()
healed = set()

def add_component(entity_id, amount):
    assert entity_id not in health
    health[entity_id] = amount

def remove_component(entity_id):
    del health[entity_id]
    try:
        del balance_change[entity_id]
    except KeyError:
        pass

def update(dt):
    global balance_change, killed, damaged, healed
    killed = set()
    damaged = set()
    healed = set()

    for entity_id, balance in balance_change.iteritems():
        current_health = health[entity_id]
        current_health += balance
        health[entity_id] = current_health
        if balance > 0:
            healed.add(entity_id)
        elif balance < 0:
            if current_health < 0:
                killed.add(entity_id)
            else:
                damaged.add(entity_id)

    balance_change = {}

def apply_damage(entity_id, amount):
    balance = balance_change.get(entity_id, 0)
    balance -= amount
    balance_change[entity_id] = balance

def heal(entity_id, amount):
    balance = balance_change.get(entity_id, 0)
    balance += amount
    balance_change[entity_id] = balance

def get_health(entity_id):
    return health[entity_id]
