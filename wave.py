import spawner, spawners, manager, entityid

def wave_01():
    first_armada = entityid.create()
    manager.create_entity(first_armada, spawners.enemy_spawner)

    yield lambda : spawner.spawn_count(first_armada) > 2

    manager.destroy_entity(first_armada)
