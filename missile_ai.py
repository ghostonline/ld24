import planar, spatial, collider, manager, explosions, entityid
import collections

missiles = {}
render_update = []

_hit = set()
_hit_data = collections.Counter()
hit = set()
hit_data = collections.Counter()

def add_component(entity_id, speed, owner):
    assert entity_id not in missiles
    missiles[entity_id] = (speed, owner)

def remove_component(entity_id):
    del missiles[entity_id]

def update(dt):
    global hit, hit_data, _hit, _hit_data
    hit = _hit
    hit_data = _hit_data
    _hit = set()
    _hit_data = collections.Counter()

    for entity_id, data in missiles.iteritems():
        speed, owner = data
        distance =  speed * dt
        spatial.move_forward(entity_id, distance)

def process_events():
    missile_ids = set(missiles)
    left_world = missile_ids.intersection(collider.world_events)
    for entity_id in left_world:
        manager.destroy_entity(entity_id)

    struck_target = missile_ids.intersection(collider.collide_events)
    for entity_id in struck_target:
        if entity_id not in missiles:
            continue
        target_ids = collider.collide_events_data[entity_id]
        owner_id = missiles[entity_id][1]
        target_ids = [id_ for id_ in target_ids if id_ != owner_id]
        if target_ids:
            position = spatial.get_position(entity_id)
            spawn_missilesplash(position)
            manager.destroy_entity(entity_id)

def spawn_missilesplash(position):
    splash_id = entityid.create()
    missile_splash['spatial']['position'] = position
    missile_splash['aoe']['data'] = position
    manager.create_entity(splash_id, missile_splash)

def apply_missile_damage(target_ids, data):
    global _hit, _hit_data
    explosions.create(data, big=True)
    map(_hit.add, target_ids)
    _hit_data.update(target_ids)

missile_splash = {
    'spatial': {
        'position': (0,0)
    },
    'collider': {
        'radius': 16,
        'player_only': False,
    },
    'aoe': {
        'func': apply_missile_damage,
        'data': None,
    },
}

