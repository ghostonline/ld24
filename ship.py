player = {
    'spatial': {
        'position': (200, 100),
        'angle': 0,
    },
    'jetengine': {
        'speed': 200,
    },
    'collider': {
        'radius': 16,
    },
    'cannon': {
        'cooldown': 0.3,
    },
    'render': {
        'image_name': "ship.png",
    },
    'health': {
        'amount':5,
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
        'image_name': "ship.png",
    },
    'health': {
        'amount':5,
    },
    'enemy_ai': None,
    'evoseed': {
        'max_health': 2
    },
}
