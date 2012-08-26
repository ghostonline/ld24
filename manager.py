import importlib

components = [
    'score',
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
    'bank',
    'render', 
    'text',
]

loaded = {
}

updatable = [
]

event_processors = [
]

exclude = ['render', 'text']

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

def create_entity(entity_id, parameters):
    for component, settings in parameters.iteritems():
        component_mod = loaded[component]
        if settings:
            component_mod.add_component(entity_id, **settings)
        else:
            component_mod.add_component(entity_id)

def destroy_entity(entity_id):
    for component in loaded.itervalues():
        try:
            component.remove_component(entity_id)
        except KeyError:
            pass
