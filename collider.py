import planar
import operator
import spatial
import player

worlds = {}

collidables = {}
world_collidables = {}

push_back_vectors = (
    planar.Vec2(1, 0),
    planar.Vec2(0, 1),
    planar.Vec2(-1, 0),
    planar.Vec2(0, -1),
)

world_events = set()
collide_events = set()
collide_lookup = {}

def set_world(name, x, y, width, height):
    origin = planar.Vec2(x,y)
    max_point = planar.Vec2(x + width, y + height)

    horizontal = planar.Vec2(1, 0)
    vertical = planar.Vec2(0, 1)
    
    left = planar.c.Line(origin, vertical)
    bottom = planar.c.Line(origin, horizontal * -1)
    right = planar.c.Line(max_point, vertical * -1)
    top = planar.c.Line(max_point, horizontal)
    worlds[name] = (left, bottom, right, top)

def add_component(entity_id, radius, world=None, player_only=False):
    assert entity_id not in collidables
    collidables[entity_id] = (radius, player_only)
    if world:
        world_collidables[entity_id] = (radius, world)

def remove_component(entity_id):
    del collidables[entity_id]
    try:
        del world_collidables[entity_id]
    except KeyError:
        pass

def update(dt):
    global world_events
    global collide_events_data
    global collide_events
    world_events = set()
    collide_events = set()
    collide_events_data = {}

    player_id = player.player_id

    for entity_id, data in world_collidables.iteritems():
        radius, world_name = data
        world = worlds[world_name]
        pos_vec = spatial.get_position_vec(entity_id)
        distances = map(lambda ray: ray.distance_to(pos_vec), world)
        push_back = [v * -(d - radius) for d,v in zip(distances, push_back_vectors) if d - radius < 0]
        if push_back:
            push_back_vec = reduce(operator.add, push_back, planar.Vec2(0,0))
            spatial.move_vec(entity_id, push_back_vec)
            world_events.add(entity_id)

    for entity_id, data in collidables.iteritems():
        radius, player_only = data
        pos_vec = spatial.get_position_vec(entity_id)

        candidates = ((id_, d) for (id_, d) in collidables.iteritems() if id_ != entity_id and (not player_only or id_ == player_id))
        for other_id, other_data in candidates:
            other_radius = other_data[0]
            other_vec = spatial.get_position_vec(other_id)
            distance = other_vec.distance_to(pos_vec) 
            if distance - other_radius - radius < 0:
                collide_events.add(entity_id)
                data = collide_events_data.get(entity_id, [])
                data.append(other_id)
                collide_events_data[entity_id] = data
