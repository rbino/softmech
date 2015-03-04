#!/usr/bin/env python
from pyxhook import HookManager
import thread
from random import choice
import os
import pyglet
import sys

sounddir="CMStormTKBlue"
pressed={}

sounds = os.listdir(sounddir)
downs = [f for f in sounds if "down.wav" in f]
ups = [f for f in sounds if "up.wav" in f]

cachedSongs = [pyglet.resource.media(sounddir + os.sep + f, streaming=False) for f in sounds]

def handle_event_down (event):
  if (event.Key not in pressed or not pressed[event.Key]):
    playrandom(downs)
  pressed[event.Key] = True

def handle_event_up (event):
  playrandom(ups)
  pressed[event.Key] = False

def playrandom(sounds):
  choice(cachedSongs).play()

hm = HookManager()
hm.HookKeyboard()
hm.KeyDown = handle_event_down
hm.KeyUp = handle_event_up
try:
  hm.run()
except:
  print
  print "Click clack! Bye!"
