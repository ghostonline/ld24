import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

import render, spatial
import entityid
import ship

def init():
    render.window = window
    player = entityid.create()
    ship.create(player)

@window.event
def on_draw():
    render.draw()

def update(dt):
    render.update()

pyglet.clock.schedule_interval(update, 1/30.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()
