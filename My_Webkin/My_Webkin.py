from microbit import *

while True:
    if (button_a.is_pressed() == True):
        display.show(Image.HAPPY)
        sleep(500)
    elif (button_b.is_pressed() == True):
        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(1000)
        break
    else:
        display.show(Image.SAD)

display.clear()
