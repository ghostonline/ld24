import spatial, render, entityid, bullet_ai, collider

def create(pos, angle, speed, image):
    bullet_id = entityid.create()
    spatial.add_component(bullet_id, pos, angle)
    render.add_component(bullet_id, image)
    bullet_ai.add_component(bullet_id, speed)
    collider.add_component(bullet_id, 0)
    return bullet_id

def destroy(entity_id):
    spatial.remove_component(entity_id)
    render.remove_component(entity_id)
    bullet_ai.remove_component(entity_id)
    collider.remove_component(entity_id)
