score = {}

total = 0
new_score = True

def add_component(entity_id, amount):
    assert entity_id not in score
    score[entity_id] = amount

def remove_component(entity_id):
    del score[entity_id]

def update(dt):
    global new_score
    new_score = False

def award(entity_id):
    global total, new_score
    amount = score[entity_id]
    total += amount
    new_score = True
