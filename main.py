import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    pass

@window.event
def on_mouse_motion(x, y, dx, dy):
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
    pass

@window.event
def on_mouse_release(x, y, button, modifiers):
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    pass

def update(dt):
    pass

pyglet.clock.schedule_interval(update, 1/30.0)

if __name__ == "__main__":
    pyglet.app.run()
