import entityid, manager

def create(pos, angle, speed, image):
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
            'speed': speed
        },
        'collider': {
            'radius': 0,
            'world': 'projectiles',
        },
    }
    manager.create_entity(bullet_id, parameters)
    return bullet_id
