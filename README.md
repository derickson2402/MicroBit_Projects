I had fun working on this project during the Covid-19 pandemic, but I am retiring this repo for now (plus I don't own a micro:bit). If you have interest in any of these projects please let me know and I can try to connect you to more resources or give you some ideas!

---

# Daniel's BBC micro:bit Repository

Welcome to my Big Ol' Repository O' Code!

Actually, it's really not that large, but it does, in fact, contain code!

Anyways, this repository contains several different projects that I am working on for a BBC micro:bit! The [micro:bit](https://www.microbit.org) is a small computing device that runs [MicroPython](https://micropython.org).

Please note that I am using the following:

- Newer micro:bit (combined compass and accelerometer chip)
- micro:bit Firmware Version 0253
- Python 3.8.1
- pip 20.0.2

And that I am not using:

- Additional, external MicroPython packages that must be flashed to the micro:bit

However, this should not affect your functionality at all, as the micro:bit is setup to run out of the box with no added packages. You may have to update the firmware for features like programming online.

Feel free to email me any questions or concerns, and please tag any bugs or errors you find! It gives me something to do with my life, which is good.


## Repository Contents

Currently I have the following projects in this repository. Each folder contains the .py python file, and a .hex executable file for the micro:bit.

- `My_Webkin` - A simple microbit.org demo project. Stroke the pins with your finger to pet the animal, and make it happy
- `DrWho_Theme` - A copy of someone else's work, connect a speaker to pin0 and ground to play the popular theme song
- `Music_Project` - A multi-part project that I created to play music over a connected speaker.

Additionally, check out the `MicroBit_Software` folder for more information, copies of firmware, lists of modules, the Out-Of-Box-Experience, and other useful pieces of micro:bit Software.


## Getting Started

Generally speaking, you can just connect a micro:bit to your computer, copy a .hex file to the external storage device labelled MICROBIT, and the device should automatically be flashed.

I recommend checking out the MicroPython documentation at [microbit.org](https://microbit.org/get-started/user-guide/python/). It will walk you through setting up your own micro:bit, and has some links if you're like me and want to dive in deaper than the basic projects.

To create your own Python script is easy. Simply go online to the [Python Editor for micro:bit](https://python.microbit.org/v/2.0), and either write your code there or paste pre-existing code. Just make sure that the beginning includes:

```
from microbit import *
```

so that the MicroPython interpreter on the micro:bit imports all of the necessary built-in modules. When the code is written, either download the .hex file, or, in Google Chrome, connect directly to the micro:bit and flash it from the webpage. Note that MicroPython is an implementation of Python 3, and as such follows the same syntax.


## uFlash

I **highly** recommend checking out uflash for programming completely within a terminal on a Unix/Linux/macOS system. You can find the documentation [here](https://uflash.readthedocs.io/en/latest/).

To install, make sure that you have Python 3.x and pip 20.0.x installed. Then use:

```
$ pip install uflash
```

...to install, and upgrade to the newest version with:

```
$ pip install --no-cache --upgrade uflash
```
