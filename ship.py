import render
import spatial
import jetengine
import cannon
import collider

def create(entity_id):
    render.add_component(entity_id, "ship.png")
    spatial.add_component(entity_id, (200, 200))
    jetengine.add_component(entity_id, 300)
    cannon.add_component(entity_id, 1)
    collider.add_component(entity_id, 16)
