import ship, cannon

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

score_dist = [
    (3, 200),
    (6, 400),
    (9, 1000),
    (12, 2000),
]

health_dist = [
    (6, 5, 3),
    (12, 7, 4),
]

weapon_dist = [
    (0, {
        'cannon': {
            'cooldown': 2,
            'player_only': True,
            'type_': cannon.DUAL
        },
    }),
    (6, {
        'cannon': {
            'cooldown': 3,
            'player_only': True,
            'type_': cannon.SPREADER
        },
    }),
    (12, {
        'launcher': {
            'cooldown': 3,
            'player_only': True,
        },
    }),
    (15, {
        'launcher': {
            'cooldown': 1,
            'player_only': True,
        },
    }),
]

def generate_enemies(level):
    odd = level % 2
    enemy = ship.enemy

    # Direction
    enemy['invader_ai']['initial_direction'] = -1 if odd else 1

    # Score
    current_score = 100
    for level_req, score in score_dist:
        if level_req < level:
            current_score = score
        else:
            break
    enemy['score']['amount'] = current_score

    # Health
    current_health, current_max = 3, 2
    for level_req, health, max_ in health_dist:
        if level_req < level:
            current_health, current_max = health, max_
        else:
            break
    enemy['health']['amount'] = current_health
    enemy['evoseed']['max_health'] = current_max

    # Weapon
    current_weapon = {}
    try:
        del enemy['cannon']
    except KeyError:
        pass
    try:
        del enemy['launcher']
    except KeyError:
        pass
    for level_req, weapon in weapon_dist:
        if level_req < level:
            current_weapon = weapon
        else:
            break
    enemy.update(current_weapon)

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

def generate_kamikaze(level):
    odd = level % 2
    kamikaze = ship.kamikaze
    kamikaze['kamikaze_ai']['attempts'] = min(level, 4)
    kamikaze['kamikaze_ai']['cooldown'] = max(4/level, 1)
    spawner = {
        'spatial': {
            'position': (192 - 128 * odd, 260),
        },
        'spawner': {
            'cooldown':2,
            'entity_data':ship.kamikaze,
        },
    }
    return spawner
