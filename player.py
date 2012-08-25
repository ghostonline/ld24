import jetengine, keyboard, cannon, bank

player_id = None

def set_player(entity_id):
    player_id = entity_id

def update(dt):
    move_me = [0, 0]
    if keyboard.key_down(keyboard.UP):
        move_me[1] += 1
    if keyboard.key_down(keyboard.DOWN):
        move_me[1] -= 1
    if keyboard.key_down(keyboard.LEFT):
        move_me[0] -= 1
    if keyboard.key_down(keyboard.RIGHT):
        move_me[0] += 1
    jetengine.move(player_id, move_me)

    move_x = move_me[0]
    if move_x > 0:
        bank.to_right(player_id)
    elif move_x < 0:
        bank.to_left(player_id)

    if keyboard.key_down(keyboard.FIRE):
        cannon.fire(player_id)

def remove_component(entity_id):
    raise KeyError(entity_id)
