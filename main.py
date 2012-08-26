import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keystate = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystate)

import render, collider, keyboard, enemy_ai, evoseed, player, text
import manager

import entityid
import ship
import gui

def init():
    manager.load_components()
    gui_id = entityid.create()
    manager.create_entity(gui_id, gui.gui)

    # Setup components
    render.window = window
    keyboard.keystate = keystate
    collider.set_world(32, 0, 192, 240)

    # Create player ship
    player_id = entityid.create()
    manager.create_entity(player_id, ship.player)
    player.player_id = player_id
    evoseed.collector_id = player_id

    # Create enemy ship
    enemy_id = entityid.create()
    manager.create_entity(enemy_id, ship.enemy)

@window.event
def on_draw():
    render.draw()
    text.draw()

def update(dt):
    manager.update(dt)
    manager.process_events()

    render.update(dt)
    text.update(dt)

pyglet.clock.schedule_interval(update, 1.0/60.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()
