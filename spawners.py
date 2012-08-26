import ship

enemy_spawner = {
    'spatial': {
        'position': (64, 260),
        'angle':180,
    },
    'spawner': {
        'cooldown':5,
        'entity_data':ship.enemy,
    },
}
