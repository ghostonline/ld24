import jetengine, keyboard, trigger, bank, health, bullet_ai, manager
import launcher, cannon, evoseed

player_id = None

spreader_upgrade_data = {
    'cooldown': 0.3,
    'type_': cannon.SPREADER
}

missile_upgrade_data = {
    'cooldown': 0.5,
    'offset': 8,
}

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
        trigger.hold(player_id)
    else:
        trigger.release(player_id)

    if player_id in bullet_ai.hit:
        damage = bullet_ai.hit_data[player_id]
        health.apply_damage(player_id, damage)

    if player_id in health.killed:
        manager.destroy_entity(player_id)
        spawn_new()

    global current_weapon, current_path_changed, current_weapon_changed
    current_path_changed = False
    current_weapon_changed = False
    requirement = get_next_upgrade_requirement()
    if requirement and requirement <= evoseed.collected:
        requirement, weapon_name, upgrade_func = current_path.pop(0) 
        upgrade_func()
        current_weapon = weapon_name
        current_path_changed = True
        current_weapon_changed = True



def remove_component(entity_id):
    raise KeyError(entity_id)

def spawn_new():
    import entityid, ship, evoseed, gui
    global player_id, current_path, current_weapon
    if not player_id:
        player_id = entityid.create()
    manager.create_entity(player_id, ship.player)
    evoseed.collector_id = player_id
    evoseed.collected = 0
    current_path = list(upgrade_path)
    current_weapon = current_standard_weapon
    gui.first_update()
    return player_id

def get_next_upgrade_requirement():
    if current_path:
        return current_path[0][0]

def spreader_upgrade():
    cannon.remove_component(player_id)
    cannon.add_component(player_id, **spreader_upgrade_data)

def missile_upgrade():
    cannon.remove_component(player_id)
    launcher.add_component(player_id, **missile_upgrade_data)

upgrade_path = (
    (10, 'spreader', spreader_upgrade),
    (20, 'missiles', missile_upgrade),
)

current_path = upgrade_path
current_path_changed = False

current_weapon = "cannon"
current_standard_weapon = "cannon"
current_weapon_changed = False
