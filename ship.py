import render
import spatial
import jetengine
import cannon
import collider

player = {
    'pos': (200, 200),
    'speed': 300,
    'radius': 16,
    'fire_rate': 0.3,
    'image': "ship.png",
    'angle': 0,
}

enemy = {
    'pos': (100, 100),
    'speed': 100,
    'radius': 16,
    'fire_rate': 1,
    'image': "ship.png",
    'angle': 180,
}

def create(entity_id, pos, angle, speed, radius, fire_rate, image):
    render.add_component(entity_id, image)
    spatial.add_component(entity_id, pos, angle)
    jetengine.add_component(entity_id, speed)
    cannon.add_component(entity_id, fire_rate)
    collider.add_component(entity_id, radius)
