import render
import spatial
import jetengine
import cannon
import collider
import health as health_comp

player = {
    'pos': (200, 100),
    'speed': 300,
    'radius': 16,
    'fire_rate': 0.3,
    'image': "ship.png",
    'angle': 0,
    'health':5,
}

enemy = {
    'pos': (100, 200),
    'speed': 100,
    'radius': 16,
    'fire_rate': 1,
    'image': "ship.png",
    'angle': 180,
    'health':5,
}

def create(entity_id, pos, angle, speed, radius, fire_rate, health, image):
    render.add_component(entity_id, image)
    spatial.add_component(entity_id, pos, angle)
    jetengine.add_component(entity_id, speed)
    cannon.add_component(entity_id, fire_rate)
    collider.add_component(entity_id, radius)
    health_comp.add_component(entity_id, health)

def destroy(entity_id):
    render.remove_component(entity_id)
    spatial.remove_component(entity_id)
    jetengine.remove_component(entity_id)
    cannon.remove_component(entity_id)
    collider.remove_component(entity_id)
    health_comp.remove_component(entity_id)
