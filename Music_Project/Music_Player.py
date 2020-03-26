from microbit import *
import music

MegaMelody = ["D4:1", "D4:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"C4:1", "C4:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"B3:1", "B3:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"A#3:1", "A#3:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1"]

def Play_Megalovania():
    music.set_tempo(ticks=16, bpm=30)
    display.show(Image.HAPPY)
    music.play(MegaMelody)

RunawayMelody = ["C6:3", "R:1", "C6:3", "R:1", "C6:3", "R:1", "C5:3", "R:1", \
"B5:3", "R:1", "B5:3", "R:1", "B5:3", "R:1", "B4:3", "R:1", \
"A5:3", "R:1", "A5:3", "R:1", "A5:3", "R:1", "A4:3", "R:1", \
"F5:3", "R:1", "F5:3", "R:1", "E5:3", "R:1", "C6:3"]

def Play_Runaway():
    music.set_tempo(ticks=8, bpm=25)
    display.show(Image.SILLY)
    music.play(RunawayMelody)

def End_Program():
    display.show(Image("12345:34567:56789:78901:90123"))
    for freq in range(3000, 400, -50):
        music.pitch(freq, 1)
    sleep(500)

ProgramRunning = True
while (ProgramRunning == True):
    if (button_a.is_pressed()):
        Play_Megalovania()
    elif (button_b.is_pressed()):
        Play_Runaway()
    display.clear()
