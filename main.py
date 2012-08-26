import pyglet
pyglet.resource.path = ['res']
pyglet.resource.reindex()

window = pyglet.window.Window()
keystate = pyglet.window.key.KeyStateHandler()
window.push_handlers(keystate)

import render, collider, keyboard, player, text
import manager

import entityid
import ship
import wave
import gui

wave_iter = None
wave_cond = lambda : True

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

    # Create player ship
    player.spawn_new()

    global wave_iter
    wave_iter = wave.wave_01()

@window.event
def on_draw():
    render.draw()
    text.draw()

def update(dt):
    if dt > 0.25:
        dt = 0.25

    global wave_iter, wave_cond
    if wave_iter and wave_cond():
        try:
            wave_cond = next(wave_iter)
        except StopIteration:
            wave_iter = None

    manager.update(dt)
    manager.process_events()

    gui.update()
    render.update(dt)
    text.update(dt)

pyglet.clock.schedule_interval(update, 1.0/60.0)

if __name__ == "__main__":
    init()
    pyglet.app.run()
