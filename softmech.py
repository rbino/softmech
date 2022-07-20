#!/usr/bin/env python
import os
from sdl2 import *
from sdl2.ext.compat import byteify
from sdl2.sdlmixer import *

import keyboard
from random import choice
import time

sounddir = "CMStormTKBlue"
pressed = {}



def handle_event(event):
    if event.event_type == keyboard.KEY_UP:
        handle_event_up(event)
    else:
        handle_event_down(event)

def handle_event_down(event):
    if (event.name not in pressed or not pressed[event.name]):
        if event.name == "space":
            playrandom(spacedowns)
        elif event.name == "backspace":
            playrandom(returndowns)
        else:
            playrandom(downs)
    pressed[event.name] = True


def handle_event_up(event):
    if event.name == "space":
        playrandom(spaceups)
    elif event.name == "backspace":
        playrandom(returnups)
    else:
        playrandom(ups)
    pressed[event.name] = False


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

keyboard.hook(handle_event, suppress=False)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClick clack! Bye!")
