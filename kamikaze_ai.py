import planar
import spatial
import player
import collider
import manager
import score
import health
import explosions

enemies = {}

IDLE, ATTACKING = range(2)

SHIP_FACE = planar.Vec2(0, 1)
SPEED = 200
DAMAGE = 5

class State:
    def __init__(self, attempts, cooldown):
        self.attempts = attempts
        self.cooldown = cooldown
        self.timeout = 0
        self.state = IDLE

def add_component(entity_id, attempts, cooldown):
    assert entity_id not in enemies
    enemies[entity_id] = State(attempts, cooldown)

def remove_component(entity_id):
    del enemies[entity_id]

def update(dt):
    for entity_id, state in enemies.iteritems():
        timeout = state.timeout - dt
        current_state = state.state
        if timeout < 0:
            if current_state == IDLE:
                player_id = player.player_id
                target_pos = spatial.get_position_vec(player_id)
                timeout = state.cooldown
                position = spatial.get_position_vec(entity_id)
                angle = SHIP_FACE.angle_to(target_pos - position)
                current_state = ATTACKING
                spatial.set_angle(entity_id, -angle)
                state.state = current_state

        if current_state == ATTACKING:
            spatial.move_forward(entity_id, SPEED * dt)
        state.timeout = timeout

def process_events():
    enemy_ids = set(enemies)
    left_world = enemy_ids.intersection(collider.world_events)
    for entity_id in left_world:
        state = enemies[entity_id]
        amount = state.attempts
        if amount:
            state.state = IDLE
        else:
            score.award(entity_id)
            manager.destroy_entity(entity_id)
        state.attempts = amount - 1

    player_hit = enemy_ids.intersection(collider.collide_events)
    for entity_id in player_hit:
        health.apply_damage(player.player_id, DAMAGE)
        position = spatial.get_position(entity_id)
        explosions.create(position, big=False)
        manager.destroy_entity(entity_id)
