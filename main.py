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

    # Setup components
    render.window = window
    keyboard.keystate = keystate
    collider.set_world('player', 32, 0, 192, 240)
    collider.set_world('projectiles', 32, -100, 192, 440)
    collider.set_world('kamikaze', -150, -150, 192 + 300, 240 + 300)

    # Create gui
    gui.create()
    gui.update()

    # Create player ship
    player_id = entityid.create()
    manager.create_entity(player_id, ship.player)
    player.player_id = player_id
    evoseed.collector_id = player_id

    # Create enemy ship
    enemy_id = entityid.create()
    manager.create_entity(enemy_id, ship.enemy)

    # Create enemy ship
    enemy_id = entityid.create()
    manager.create_entity(enemy_id, ship.kamikaze)

@window.event
def on_draw():
    render.draw()
    text.draw()

def update(dt):
    if dt > 0.25:
        dt = 0.25

    manager.update(dt)
    manager.process_events()

    gui.update()
    render.update(dt)
    text.update(dt)

pyglet.clock.schedule_interval(update, 1.0/60.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()
