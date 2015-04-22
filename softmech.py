#!/usr/bin/env python
from pyxhook import HookManager
from random import choice
import os
from sdl2 import *
from sdl2.ext.compat import byteify
from sdl2.sdlmixer import *


sounddir = "CMStormTKBlue"
pressed = {}


def handle_event_down(event):
    if (event.Key not in pressed or not pressed[event.Key]):
        if event.Key == "space":
            playrandom(spacedowns)
        elif event.Key == "Return":
            playrandom(returndowns)
        else:
            playrandom(downs)
    pressed[event.Key] = True


def handle_event_up(event):
    if event.Key == "space":
        playrandom(spaceups)
    elif event.Key == "Return":
        playrandom(returnups)
    else:
        playrandom(ups)
    pressed[event.Key] = False


def playrandom(sounds):
    Mix_PlayChannel(-1, choice(sounds), 0)


SDL_Init(SDL_INIT_AUDIO)
Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 1, 256)
sounds = os.listdir(sounddir)
downs = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
         for f in sounds
         if "down.wav" in f]
ups = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
       for f in sounds
       if "up.wav" in f]
spacedowns = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
         for f in sounds
         if "down_space.wav" in f]
spaceups = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
       for f in sounds
       if "up_space.wav" in f]
returndowns = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
         for f in sounds
         if "down_return.wav" in f]
returnups = [Mix_LoadWAV(byteify(sounddir + os.sep + f, 'utf-8'))
       for f in sounds
       if "up_return.wav" in f]

hm = HookManager()
hm.HookKeyboard()
hm.KeyDown = handle_event_down
hm.KeyUp = handle_event_up

try:
    hm.run()
except:
    print("\nClick clack! Bye!")
