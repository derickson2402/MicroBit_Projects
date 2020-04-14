# Music Project

These programs utilize the built-in music modules on the micro:bit, which allows for audio playback using PWM on any 1 of the 3 pins. Simply pass a list where each note is a string, set up like:

```
"Note Name" + "Octave" + ":" + "Ticks" = "C4:4"
```

**Please note** that Python lists take up ~100 bytes of memory, and each element adds ~24 bytes. The micro:bit only has 16kB of onboard RAM, about 8kB of which is actually usable. Therefore, not many songs are preloaded in the software, as memory allocation errors are easy to produce.

## Music_Player

This program simply plays whatever song you feed it. Built in songs include:

- Runaway - by Kanye West
- Megalovania - from Undertale

Create your own list in the software, plug it in to the function, and have some fun!

## MultiPin_Playback

This is where the fun begins!

The MultiPin_Playback program allows two independent songs to be played simultaneously by the microbit! Normally, the microbit can only output audio to one pin at a time, and cannot run parallel processes unless you use Java and have way more patience than me. By alternating between two songs as fast as possible (about 1ms), both songs appear to play simultaneously. It sounds kinda gross, but hey, it's  neat.

**TL:DR**: I spent way too much time making a mediocre solution to play 2 songs at the same time. Enjoy!

The program is largely intended for playing a harmony and a melody, and for logistic reasons the songs must be the same length or else an error will occur.

Other than that, simply enter both songs, the ticks per beat, and the BPM of the song to get started.

