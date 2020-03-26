from microbit import *
import music

#Mega_Melody = ["D4:1", "D4:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
#"C4:1", "C4:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
#"B3:1", "B3:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
#"A#3:1", "A#3:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1"]
#Mega_Harmony = ["D4:16", "R:1", "C4:16", "R:1", "B3:16", "R:1", "A#3:1", "R:1", ]

RunawayMelody = ["C6:3", "R:1", "C6:3", "R:1", "C6:3", "R:1", "C5:3", "R:1", \
"B5:3", "R:1", "B5:3", "R:1", "B5:3", "R:1", "B4:3", "R:1", \
"A5:3", "R:1", "A5:3", "R:1", "A5:3", "R:1", "A4:3", "R:1", \
"F5:3", "R:1", "F5:3", "R:1", "E5:3", "R:1", "C6:3"]

Mega_Melody = ["C4:1", "D4:1", "E4:1"]
Mega_Harmony = ["E4:1", "D4:1", "C4:1"]
def Create_Millisecond_Music(Song, Ticks, BPM):
    #For every element of original list, convert it into the actual pitch and
    #millisecond value, creating individual entries for each millisecond
    Millisecond_Music = []
    iteration = 0
    while (iteration < len(Song)):
        Current_Element = str(Song[iteration])
        Current_Note = Current_Element[0:(Current_Element.find(':') + 1)] + '1'
        #print("\n\n\nCurrent Note is:", Current_Note, ", which is type:", type(Current_Note), type(iteration), type(len(Song)))
        Tick_Length_In_Ms = (int(60000/BPM/Ticks))
        #print("Tick Length in MS:", Tick_Length_In_Ms, "Type:", type(Tick_Length_In_Ms))
        Ticks_To_Play = int(Current_Element[(Current_Element.find(':')+1):])
        #print("Ticks_To_Play:", Ticks_To_Play, "Type:", type(Ticks_To_Play))
        #print("Arguement type is:", type(Tick_Length_In_Ms* Ticks_To_Play))
        for i in range(0, (Tick_Length_In_Ms* Ticks_To_Play), 1):
            Millisecond_Music.append(Current_Note)
        iteration += 1
    return(Millisecond_Music)

def Play_Dual_Sound(Song1, Song2, Ticks, BPM):
    #Create the new arrays, and alternate between them every millisecond
    Song1_Millisecond_Music = Create_Millisecond_Music(Song1, Ticks, BPM)
    Song2_Millisecond_Music = Create_Millisecond_Music(Song2, Ticks, BPM)
    music.set_tempo(ticks=100, bpm=600)
    print("Error: Songs are different lengths") if (len(Song1_Millisecond_Music) != len(Song2_Millisecond_Music)) else (print("Song1:\n", Song1_Millisecond_Music, '\n'*5, "Song2:\n", Song2_Millisecond_Music))
    index = 0
    while (index < len(Song1_Millisecond_Music)):
        music.play(Song1_Millisecond_Music[index], pin=pin0)
        try:
            music.play(Song2_Millisecond_Music[index+1], pin=pin1)
        except:
            print("Indexing error in the second song list")
        index+=2

def Play_Megalovania():
    display.show(Image.HAPPY)
    music.play(Mega_Melody, pin=pin1)

def End_Program():
    display.show(Image("90009:09090:00900:09090:90009"))
    for freq in range(1600, 800, -50):
        music.pitch(freq, 5)
    sleep(1000)

ProgramRunning = True
while (ProgramRunning == True):
    if (button_a.is_pressed()):
        Play_Dual_Sound(Mega_Melody, Mega_Harmony, 16, 30)
    elif (button_b.is_pressed()):
        End_Program()
        ProgramRunning = False
    display.clear()
