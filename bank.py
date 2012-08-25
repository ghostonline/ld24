import render

bankables = {}
active = {}

class State:
    def __init__(self, frames, frametime):
        self.frames = frames
        self.current = int(frames / 2)
        self.target = self.current
        self.frametime = frametime
        self.timeout = 0

def add_component(entity_id, frames, frametime):
    assert entity_id not in bankables
    bankables[entity_id] = State(frames, frametime)

def remove_component(entity_id):
    del bankables[entity_id]

def animate_to(entity_id, func):
    state = bankables[entity_id]
    state.target = func(0, state.frames - 1)
    if state.target != state.current:
        active[entity_id] = state

def to_left(entity_id):
    animate_to(entity_id, min)

def to_right(entity_id):
    animate_to(entity_id, max)

def update(dt):
    stopme = []
    for entity_id, state in active.iteritems():
        timeout = state.timeout
        timeout -= dt
        if timeout < 0:
            current = state.current
            target = state.target
            diff = current - target
            go = 0
            if diff:
                if diff < 0:
                    go = 1
                else:
                    go = -1
            current += go
            timeout = state.frametime
            state.current = current
            render.set_frame(entity_id, current)
            state.target = int(state.frames / 2)
            if current == state.target:
                stopme.append(entity_id)
        state.timeout = timeout

    for entity_id in stopme:
        del active[entity_id]

