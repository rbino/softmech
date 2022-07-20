softmech
=====
This is a little Python script that plays a random sound whenever a key is pressed/released. Specifically, I sampled my CMStorm Quickfire TK with Blue Cherry switches.
Use it to annoy people when you don't have a mechanical keyboard with you.
### Dependencies
To install dependencies (Ubuntu 20.04):

```sh
$ sudo apt-get install libsdl2-2.0
$ pip install -r requirements.txt
```
### Launching (needs root)
```sh
$ sudo ./softmech.py
```
### Additional sounds
If you want to add your own sounds just put them in a folder and change the `sounddir` variable.
Sounds to be played on KeyDown must end with "down.wav", sounds to be played on KeyUp must end with "up.wav"
