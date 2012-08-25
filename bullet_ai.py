import planar, spatial, render

bullets = {}
render_update = []

class BulletState:
    def __init__(self, angle, trajectory, speed):
        self.angle = angle
        self.trajectory = trajectory
        self.speed = speed

def add_component(entity_id, angle, speed):
    assert entity_id not in bullets

    trajectory = planar.Vec2(0, 1).rotated(-angle)
    bullets[entity_id] = BulletState(angle, trajectory, speed)
    render_update.append(entity_id)

def update(dt):
    global render_update
    for entity_id in render_update:
        angle = bullets[entity_id].angle
        render.set_rotation(entity_id, angle)
    render_update = []

    for entity_id, state in bullets.iteritems():
        trajectory = state.trajectory
        speed = state.speed
        move_vec = trajectory * speed * dt
        spatial.move_vec(entity_id, move_vec)