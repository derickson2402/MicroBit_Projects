from microbit import *
import music

#Ticks=16, BPM=30
Mega_Melody = ["D4:1", "D4:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
"C4:1", "C4:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
"B3:1", "B3:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1", \
"A#3:1", "A#3:1", "D5:2", "R:1", "A4:2", "R:1", "G#4:1", "R:1", "G4:2", "F4:2", "D4:1", "F4:1", "G4:1"]

#Ticks=16, BPM=30
Mega_Harmony = ["D4:16", "R:1", "C4:16", "R:1", "B3:16", "R:1", "A#3:16", "R:1", ]

#Ticks=8, BPM=25
RunawayMelody = ["C6:3", "R:1", "C6:3", "R:1", "C6:3", "R:1", "C5:3", "R:1", \
"B5:3", "R:1", "B5:3", "R:1", "B5:3", "R:1", "B4:3", "R:1", \
"A5:3", "R:1", "A5:3", "R:1", "A5:3", "R:1", "A4:3", "R:1", \
"F5:3", "R:1", "F5:3", "R:1", "E5:3", "R:1", "C6:3"]

def Create_Single_Step_List(Old_List):
    #Take original song List as arguement, and initialize new empty List.
    #Check original song, and append n new notes to the new list, remove from beginning of old list to save memory
    New_List = []
    while (len(Old_List) > 0):
        Song_Element = Old_List[0]
        Note = str(Song_Element[0:(Song_Element.find(':'))])
        Note_Length = int(Song_Element[(Song_Element.find(':') + 1):])
        for foo in range(0, Note_Length, 1):
            New_List.append(Note + ":1")
        del Old_List[0]
    del Old_List
    return(New_List)

def MultiPin_Playback(Song1, Song2, Ticks, BPM):
    #Pass both songs through Function to create new Lists
    #Create for loop that runs half as many times as there are milliseconds to be played
    Single_Step_Melody = Create_Single_Step_List(Song1)
    Single_Step_Harmony = Create_Single_Step_List(Song2)
    iteration = 0
    music.set_tempo(ticks=Ticks, bpm=BPM)
    while (iteration < len(Single_Step_Melody)):
        for spam in range(0,int(60000/BPM/Ticks/2),1):
            music.play(Single_Step_Melody[iteration], wait=False, pin=pin0)
            sleep(1)
            try:
                music.play(Single_Step_Harmony[iteration], wait=False, pin=pin1)
            except:
                pass
            sleep(1)
        iteration += 1
    music.stop(pin0)
    music.stop(pin1)

def Play_Song(Song, Ticks, BPM, Display_Image):
    display.show(Display_Image)
    print("Now playing:", str(Song), ", arranged by Daniel Erickson!")
    music.set_tempo(ticks=Ticks, bpm=BPM)
    music.play(Song, pin=pin0)

def End_Program():
    display.show(Image("90009:09090:00900:09090:90009"))
    for freq in range(1600, 800, -50):
        music.pitch(freq, 5)
    sleep(1000)
    quit("The program has been ended\n\nGoodby!")


#Oh yeah, this is big brain
while ((False != False) != (True == (2+2==4))):
    if (button_a.is_pressed()):
        display.show(Image.HAPPY)
        MultiPin_Playback(Mega_Melody, Mega_Harmony, 16, 30)
    elif (button_b.is_pressed()):
        Play_Song(Mega_Melody, 16, 30, Image.HAPPY)
    display.clear()
