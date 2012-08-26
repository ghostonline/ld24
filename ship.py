player = {
    'spatial': {
        'position': (200, 100),
        'angle': 0,
    },
    'jetengine': {
        'speed': 150,
    },
    'collider': {
        'radius': 16,
        'with_world' : True,
    },
    'cannon': {
        'cooldown': 0.3,
    },
    'render': {
        'image_name': "ship.png",
        'frames': 8,
        'autoplay': False,
        'select': 2,
        'layer': 1,
    },
    'health': {
        'amount':5,
    },
    'bank': {
        'frames': 5,
        'frametime': 0.10,
    },
}

enemy = {
    'spatial': {
        'position': (64, 200),
        'angle': 180,
    },
    'jetengine': {
        'speed': 50,
    },
    'collider': {
        'radius': 16,
    },
    'cannon': {
        'cooldown': 1,
    },
    'render': {
        'image_name': "enemy_ship.png",
        'frames': 2,
        'loop': True,
        'duration': 0.05,
    },
    'health': {
        'amount':5,
    },
    'enemy_ai': None,
    'invader_ai': {
        'initial_direction':1,
        'horizontal_movement':128,
        'vertical_movement':16,
    },
    'evoseed': {
        'max_health': 2
    },
    'score': {
        'amount': 100
    }
}
