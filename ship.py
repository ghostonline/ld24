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
        'position': (100, 200),
        'angle': 180,
    },
    'jetengine': {
        'speed': 100,
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
    'evoseed': {
        'max_health': 2
    },
    'score': {
        'amount': 100
    }
}
