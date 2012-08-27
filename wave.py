import spawner, spawners, manager, entityid, counter

level = 1

def wave_01():
    armada = entityid.create()
    global level
    while True:

        level_spawner = spawners.generate_enemies(level)
        manager.create_entity(armada, level_spawner)

        yield lambda : spawner.spawn_count(armada) > level - 1

        manager.destroy_entity(armada)

        yield lambda : not counter.get_count()

        level_spawner = spawners.generate_kamikaze(level)
        manager.create_entity(armada, level_spawner)

        yield lambda : spawner.spawn_count(armada) > level - 1

        manager.destroy_entity(armada)

        yield lambda : not counter.get_count()

        level += 1

