import jetengine, keyboard, cannon, bank, health, bullet_ai, manager

player_id = None

def set_player(entity_id):
    player_id = entity_id

def update(dt):
    global player_id

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

    if player_id in bullet_ai.hit:
        damage = bullet_ai.hit_data[player_id]
        health.apply_damage(player_id, damage)

    if player_id in health.killed:
        manager.destroy_entity(player_id)
        spawn_new()

def remove_component(entity_id):
    raise KeyError(entity_id)

def spawn_new():
    import entityid, ship, evoseed, gui
    global player_id
    if not player_id:
        player_id = entityid.create()
    manager.create_entity(player_id, ship.player)
    evoseed.collector_id = player_id
    gui.first_update()
    return player_id

def instant_death():
    manager.destroy_entity(player_id)
    spawn_new()
