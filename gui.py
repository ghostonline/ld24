import manager, entityid, text, score as score_mod, player, health

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
        'position': (256, 240 - 24),
        'angle': 0,
    },
}

score = {
    'text': {
        'text': ""
    },
    'spatial': {
        'position': (256, 240 - 32),
        'angle': 0,
    },
}

shield_label = {
    'text': {
        'text': "shield"
    },
    'spatial': {
        'position': (256, 240 - 48),
        'angle': 0,
    },
}

shield = {
    'text': {
        'text': "[>>>>>>>>>>]"
    },
    'spatial': {
        'position': (256, 240 - 56),
        'angle': 0,
    },
}

score_id = 0
shield_id = 0

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

def update():
    if score_mod.new_score:
        score_str = "%010d" % score_mod.total
        text.set_text(score_id, score_str)

    player_id = player.player_id
    if player_id in health.damaged or player_id in health.healed:
        current_health = health.get_health(player_id)
        shield_str = ">" * current_health
        text.set_text(shield_id, "[%s]" % shield_str)

def first_update():
    score_str = "%010d" % score_mod.total
    text.set_text(score_id, score_str)

    player_id = player.player_id
    current_health = health.get_health(player_id)
    shield_str = ">" * current_health
    text.set_text(shield_id, "[%s]" % shield_str)
