import manager, entityid, text, score as score_mod

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

score_id = 0

def create():
    gui_id = entityid.create()
    manager.create_entity(gui_id, gui)

    score_label_id = entityid.create()
    manager.create_entity(score_label_id, score_label)

    global score_id
    score_id = entityid.create()
    manager.create_entity(score_id, score)

def update():
    if score_mod.new_score:
        score_str = "%010d" % score_mod.total
        text.set_text(score_id, score_str)
