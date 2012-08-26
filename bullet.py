import entityid, manager

def create(pos, angle, speed, image, owner, player_only):
    bullet_id = entityid.create()
    parameters = {
        'spatial': {
            'position': pos,
            'angle': angle,
        },
        'render': {
            'image_name': image
        },
        'bullet_ai': {
            'speed': speed,
            'owner': owner,
        },
        'collider': {
            'radius': 0,
            'world': 'projectiles',
            'player_only': player_only,
        },
    }
    manager.create_entity(bullet_id, parameters)
    return bullet_id

def create_missile(pos, angle, speed, image, owner, player_only):
    bullet_id = entityid.create()
    parameters = {
        'spatial': {
            'position': pos,
            'angle': angle,
        },
        'render': {
            'image_name': image
        },
        'missile_ai': {
            'speed': speed,
            'owner': owner,
        },
        'collider': {
            'radius': 4,
            'world': 'projectiles',
            'player_only': player_only,
        },
    }
    manager.create_entity(bullet_id, parameters)
    return bullet_id
