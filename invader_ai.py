import spatial, jetengine, manager, explosions

enemies = {}

STATE_HORIZONTAL, STATE_VERTICAL = range(2)
DESTROY_THRESHOLD_Y = -100

class State:
    def __init__(self, initial_direction, horizontal_movement, vertical_movement):
        self.horizontal_movement = horizontal_movement
        self.vertical_movement = vertical_movement
        self.state = STATE_VERTICAL
        self.target = None
        self.direction = -1
        self.next_direction = initial_direction

def add_component(entity_id, initial_direction, horizontal_movement, vertical_movement):
    assert entity_id not in enemies
    enemies[entity_id] = State(initial_direction, horizontal_movement, vertical_movement)

def remove_component(entity_id):
    del enemies[entity_id]

def update(dt):
    destroy_me = []
    for entity_id, state in enemies.iteritems():
        position = spatial.get_position(entity_id)
        direction = state.direction
        if state.state == STATE_HORIZONTAL:
            relevant_axis = position[0]
            relevant_movement = state.horizontal_movement
            move_direction = [direction, 0]
            next_state = STATE_VERTICAL
            next_nextdirection = direction * -1
        elif state.state == STATE_VERTICAL:
            relevant_axis = position[1]
            relevant_movement = state.vertical_movement
            move_direction = [0, direction]
            next_state = STATE_HORIZONTAL
            next_nextdirection = -1

        target = state.target
        if target is None:
            target = relevant_axis + relevant_movement * direction

        distance = (target - relevant_axis) * direction
        jetengine.move(entity_id, move_direction)
        if distance < 0:
            target = None
            state.state = next_state
            state.next_direction, state.direction = next_nextdirection, state.next_direction
            if position[1] < DESTROY_THRESHOLD_Y:
                destroy_me.append(entity_id)

        state.target = target

    for entity_id in destroy_me:
        manager.destroy_entity(entity_id)
