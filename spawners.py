import ship

wave01_spawner = {
    'spatial': {
        'position': (64, 260),
        'angle':180,
    },
    'spawner': {
        'cooldown':5,
        'entity_data':ship.enemy,
    },
}

wave02_spawner = {
    'spatial': {
        'position': (196 - 64, 260),
        'angle':180,
    },
    'spawner': {
        'cooldown':0.3,
        'entity_data':ship.kamikaze,
    },
}

def generate_enemies(level):
    odd = level % 2
    enemy = ship.enemy
    enemy['invader_ai']['initial_direction'] = -1 if odd else 1
    spawner = {
        'spatial': {
            'position': (64 + 128 * odd, 260),
            'angle':180,
        },
        'spawner': {
            'cooldown':5,
            'entity_data':enemy,
        },
    }
    return spawner
