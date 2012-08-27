import manager, entityid, text, score as score_mod, player, health, evoseed

GUI_Y_START = 244

gui = {
    'spatial': {
        'position': (160, 120),
        'angle': 0,
    },
    'render': {
        'image_name': "ingamehud.png",
        'layer': 99,
    },
}

clouds = {
    'spatial': {
        'position': (128, 304),
    },
    'render': {
        'image_name': "cloudlayer_1.png",
        'layer': -2,
    },
    'mover': {
        'distance': 240,
        'speed': 50,
    },
}

clouds2 = {
    'spatial': {
        'position': (128, 960 / 2),
    },
    'render': {
        'image_name': "cloudlayer_2.png",
        'layer': -1,
    },
    'mover': {
        'distance': 480,
        'speed': 100,
    },
}

clouds3 = {
    'spatial': {
        'position': (128, 960 / 2 + 960),
    },
    'render': {
        'image_name': "cloudlayer_2.png",
        'layer': -1,
    },
    'mover': {
        'distance': 480,
        'speed': 100,
    },
}

score_label = {
    'text': {
        'text': "score"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 24),
        'angle': 0,
    },
}

score = {
    'text': {
        'text': ""
    },
    'spatial': {
        'position': (256, GUI_Y_START - 32),
        'angle': 0,
    },
}

shield_label = {
    'text': {
        'text': "shield"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 48),
        'angle': 0,
    },
}

shield = {
    'text': {
        'text': "[>>>>>>>>>>]"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 56),
        'angle': 0,
    },
}

weapon_label = {
    'text': {
        'text': "weapon"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 72),
        'angle': 0,
    },
}

weapon = {
    'text': {
        'text': "missiles"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 80),
        'angle': 0,
    },
}

progress_label = {
    'text': {
        'text': "evo target"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 96),
        'angle': 0,
    },
}

progress = {
    'text': {
        'text': "0"
    },
    'spatial': {
        'position': (256, GUI_Y_START - 104),
        'angle': 0,
    },
}

score_id = 0
shield_id = 0
weapon_id = 0
progress_id = 0

def _create_entity(dict_name):
    entity_id = entityid.create()
    data = globals()[dict_name]
    manager.create_entity(entity_id, data)
    return entity_id


def create():
    gui_id = entityid.create()
    manager.create_entity(gui_id, gui)

    cloud_id = _create_entity('clouds')
    cloud_id = _create_entity('clouds2')
    cloud_id = _create_entity('clouds3')

    score_label_id = entityid.create()
    manager.create_entity(score_label_id, score_label)

    global score_id
    score_id = entityid.create()
    manager.create_entity(score_id, score)

    global shield_id
    shield_label_id = _create_entity('shield_label')
    shield_id = _create_entity('shield')

    global weapon_id
    weapon_label_id = _create_entity('weapon_label')
    weapon_id = _create_entity('weapon')

    global progress_id
    progress_label_id = _create_entity('progress_label')
    progress_id = _create_entity('progress')

def update():
    if score_mod.new_score:
        score_str = "%010d" % score_mod.total
        text.set_text(score_id, score_str)

    player_id = player.player_id
    if player_id in health.damaged or player_id in health.healed:
        current_health = health.get_health(player_id)
        shield_str = ">" * current_health
        text.set_text(shield_id, "[%s]" % shield_str)

    if evoseed.collected_change or player.current_path_changed:
        requirement = player.get_next_upgrade_requirement()
        if requirement:
            collected_str = "%d" % (requirement - evoseed.collected)
        else:
            collected_str = "maximum"
        text.set_text(progress_id, collected_str)

    if player.current_weapon_changed:
        text.set_text(weapon_id, player.current_weapon)

def first_update():
    score_str = "%010d" % score_mod.total
    text.set_text(score_id, score_str)

    player_id = player.player_id
    current_health = health.get_health(player_id)
    shield_str = ">" * current_health
    text.set_text(shield_id, "[%s]" % shield_str)

    requirement = player.get_next_upgrade_requirement()
    if requirement:
        collected_str = "%d" % (requirement - evoseed.collected)
    else:
        collected_str = "at maximum"
    text.set_text(progress_id, collected_str)

    text.set_text(weapon_id, player.current_weapon)
