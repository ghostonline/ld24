health = {}
balance_change = {}

killed = set()
damaged = set()
healed = set()

class State:
    def __init__(self, health, vurnable):
        self.health = health
        self.vurnable = vurnable

def add_component(entity_id, amount):
    assert entity_id not in health
    health[entity_id] = State(amount, True)

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
        state = health[entity_id]
        if not state.vurnable:
            continue
        state.health += balance
        if balance > 0:
            healed.add(entity_id)
        elif balance < 0:
            if state.health < 0:
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
    return health[entity_id].health

def set_vurnable(entity_id, value):
    state = health[entity_id]
    state.vurnable = value
