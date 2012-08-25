import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keystate = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystate)

import render, spatial, keyboard, player, jetengine, cannon
import entityid
import ship

def init():
    # Setup components
    render.window = window
    keyboard.keystate = keystate

    # Create player ship
    player_id = entityid.create()
    ship.create(player_id)
    player.player_id = player_id

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
    player.update()
    jetengine.update(dt)
    cannon.update(dt)
    render.update()

pyglet.clock.schedule_interval(update, 1.0/60.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()