import render
import spatial
import jetengine

def create(entity_id):
    render.add_component(entity_id, "ship.png")
    spatial.add_component(entity_id, (200, 200))
    jetengine.add_component(entity_id, 300)
