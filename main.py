import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keystate = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystate)

import render, collider, keyboard, enemy_ai, evoseed, player
import manager

import entityid
import ship

def init():
    manager.load_components()

    # Setup components
    render.window = window
    keyboard.keystate = keystate
    collider.set_world(320, 240)

    # Create player ship
    player_id = entityid.create()
    manager.create_entity(player_id, ship.player)
    player.player_id = player_id
    evoseed.collector_id = player_id

    # Create enemy ship
    enemy_id = entityid.create()
    manager.create_entity(enemy_id, ship.enemy)

def setup_opengl():
    pyglet.gl.glLoadIdentity()
    pyglet.gl.glScalef(2.0, 2.0, 1.0)
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D,
        pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D,
        pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

@window.event
def on_draw():
    setup_opengl()
    render.draw()

def update(dt):
    manager.update(dt)
    manager.process_events()

    render.update(dt)

pyglet.clock.schedule_interval(update, 1.0/60.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()
