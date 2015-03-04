softmech
=====
This is a little Python script that plays a random sound whenever a key is pressed/released. Specifically, I sampled my CMStorm Quickfire TK with Blue Cherry switches.  
Use it to annoy people when you don't have a mechanical keyboard with you.
### Dependencies
To install dependencies (on Debian):
```sh
$ sudo apt-get install python-xlib
```
### Launching
```sh
$ chmod +x softmech.py
$ ./softmech.py
```
### Additional sounds
If you want to add your own sounds just put them in a folder and change the `sounddir` variable.  
Sounds to be played on KeyDown must end with "down.wav", sounds to be played on KeyUp must end with "up.wav"
