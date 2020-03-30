from microbit import *
import music

#Ticks=16, BPM=30
Megalovania = ["D4:1", "D4:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"C4:1", "C4:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"B3:1", "B3:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1", \
"A#3:1", "A#3:1", "D5:1", "R:1", "A4:1", "R:1", "G#4:2", "G4:2", "F4:3", "D4:1", "F4:1", "G4:1"]

#Ticks=8, BPM=25
Runaway = ["C6:3", "R:1", "C6:3", "R:1", "C6:3", "R:1", "C5:3", "R:1", \
"B5:3", "R:1", "B5:3", "R:1", "B5:3", "R:1", "B4:3", "R:1", \
"A5:3", "R:1", "A5:3", "R:1", "A5:3", "R:1", "A4:3", "R:1", \
"F5:3", "R:1", "F5:3", "R:1", "E5:3", "R:1", "C6:3"]

def Play_Song(Song, Ticks, BPM, Display_Image):
    display.show(Display_Image)
    print("Now playing:", str(Song), ", arranged by Daniel Erickson!")
    music.set_tempo(ticks=Ticks, bpm=BPM)
    music.play(Song, pin=pin0)

def End_Program():
    display.show(Image("12345:34567:56789:78901:90123"))
    for freq in range(3000, 400, -50):
        music.pitch(freq, 1)
    sleep(1000)
    quit("The program has been terminated\n\nGoodbye!")

ProgramRunning = True
while (ProgramRunning == True):
    if (button_a.is_pressed()):
        Play_Song(Megalovania, 16, 30, Image.HAPPY)
    elif (button_b.is_pressed()):
        Play_Song(Runaway, 8, 25, Image.SILLY)
    display.clear()
