import planar
import operator
import spatial

world = None

collidables = {}
push_back_vectors = (
    planar.Vec2(1, 0),
    planar.Vec2(0, 1),
    planar.Vec2(-1, 0),
    planar.Vec2(0, -1),
)

events = set()

def set_world(width, height):
    global world
    origin = planar.Vec2(0,0)
    max_point = planar.Vec2(width, height)

    horizontal = planar.Vec2(1, 0)
    vertical = planar.Vec2(0, 1)
    
    left = planar.c.Line(origin, vertical)
    bottom = planar.c.Line(origin, horizontal * -1)
    right = planar.c.Line(max_point, vertical * -1)
    top = planar.c.Line(max_point, horizontal)
    world = (left, bottom, right, top)

def add_component(entity_id, radius):
    assert entity_id not in collidables
    collidables[entity_id] = radius

def remove_component(entity_id):
    del collidables[entity_id]

def update():
    global events
    events = set()
    for entity_id, radius in collidables.iteritems():
        pos_vec = spatial.get_position_vec(entity_id)
        distances = map(lambda ray: ray.distance_to(pos_vec), world)
        push_back = [v * -(d - radius) for d,v in zip(distances, push_back_vectors) if d - radius < 0]
        if push_back:
            push_back_vec = reduce(operator.add, push_back, planar.Vec2(0,0))
            spatial.move_vec(entity_id, push_back_vec)
            events.add(entity_id)
