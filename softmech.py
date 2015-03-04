#!/usr/bin/env python
from pyxhook import HookManager
import thread
from random import choice
import os

sounddir="CMStormTKBlue"
pressed={}

def handle_event_down (event):
  if (event.Key not in pressed or not pressed[event.Key]):
    playrandom(downs)
  pressed[event.Key] = True

def handle_event_up (event):
  playrandom(ups)
  pressed[event.Key] = False

def playrandom(sounds):
  thread.start_new_thread(os.system,("cat " + sounddir + os.sep + choice(sounds) + " | aplay -q -f cd",))

sounds = os.listdir(sounddir)
downs = [f for f in sounds if "down.wav" in f]
ups = [f for f in sounds if "up.wav" in f]
hm = HookManager()
hm.HookKeyboard()
hm.KeyDown = handle_event_down
hm.KeyUp = handle_event_up
try:
  hm.run()
except:
  print
  print "Click clack! Bye!"
