import importlib

components = [
    'player',
    'keyboard',
    'jetengine',
    'cannon',
    'bullet_ai',
    'enemy_ai',
    'health',
    'evoseed',
    'spatial',
    'collider',
    'render', 
]

loaded = {
}

updatable = [
]

event_processors = [
]

exclude = ['render']

def load_components():
    global loaded, updatable, event_processors
    loaded = {}
    updatable = []
    event_processors = []

    for component in components:
        mod = importlib.import_module(component)
        loaded[component] = mod

        if component in exclude:
            continue

        if hasattr(mod, "update"):
            updatable.append(mod)
            
        if hasattr(mod, "process_events"):
            event_processors.append(mod)

def update(dt):
    for component in updatable:
        component.update(dt)

def process_events():
    for component in event_processors:
        component.process_events()
