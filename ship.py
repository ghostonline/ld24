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
        'world' : 'player',
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
        'amount':10,
    },
    'bank': {
        'frames': 5,
        'frametime': 0.10,
    },
    'forcefield': {
        'timeout': 5
    }
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
    },
    'counter': None,
}

kamikaze = {
    'spatial': {
        'position': (-100, 50),
        'angle': 0,
    },
    'collider': {
        'radius': 4,
        'world':'kamikaze',
        'player_only': True,
    },
    'render': {
        'image_name': "kamikaze.png",
    },
    'kamikaze_ai': {
        'attempts':3,
        'cooldown':4,
    },
    'score': {
        'amount': 300
    },
    'counter': None,
}
