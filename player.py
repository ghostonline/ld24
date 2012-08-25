import spatial, keyboard
import planar

player_id = None
player_speed = 300

def set_player(entity_id):
    player_id = entity_id

def update(dt):
    move_speed = dt * player_speed
    move_me = [0, 0]
    if keyboard.key_down(keyboard.UP):
        move_me[1] += 1 * move_speed
    if keyboard.key_down(keyboard.DOWN):
        move_me[1] -= 1 * move_speed
    if keyboard.key_down(keyboard.LEFT):
        move_me[0] -= 1 * move_speed
    if keyboard.key_down(keyboard.RIGHT):
        move_me[0] += 1 * move_speed
    spatial.move_vec(player_id, move_me)
