from music import pitch, stop
from microbit import sleep, display, pin1

notes = {
        'r': None,
        'd2': 73,
        'e2': 82,
        'fs2': 93,
        'g2': 98,
        'a2': 110,
        'b2': 123,
        'c': 131,
        'd': 147,
        'e': 165,
        'f': 175,
        'fs': 185,
        'g': 196
    }
types = { '': 21, '1': 28 }

patterns = [
  lambda args: '%s.3.:%s.1.:' % (args[0], args[1]),
  lambda args: '%s.3.:%s.1.:' % (args[0], args[0]),
  lambda args: '%s.3.:%s.1.:%s.3.:%s.1.:' % (args[0], args[0], args[0], args[1]),
  lambda args: '%s.3.:%s.1.:%s.3.:%s.1.:' % (args[0], args[0], args[0], args[0])
]

pattern = ''

# A
pattern += 'd.1.:' + ('p.2.e,d:'*2 + 'p.2.e,fs:p.2.g,d:')*2 + 'e.7.:d.1.:'*2 + 'e.7.:fs.1.:g.4.1:f.1.1:d.1.1:' + 'e.7.:d.1.:'*2 + 'e.7.:fs.1.:p.1.g:p.1.fs:'

# B
pattern += 'p.2.e,d:p.2.e,a2:p.2.b2,a2:p.0.b2,b2:b2.1.1:c.1.1:d.1.1:'*2

# C
pattern += 'p.2.e,d:p.2.e,fs:p.2.g,a2:p.1.b2:b2.1.1:c.1.1:d.1.1:e.4.:a2.4.:b2.4.1:c.1.1:d.1.1:' + ('p.2.b2,a2:'*2 + 'p.2.b2,c:p.1.d:d.1.1:c.1.1:a2.1.1:')*2

# D
pattern += 'p.2.g2,fs2:'*3 + 'p.3.g2:' + 'p.3.d2:'
pattern += 'p.2.g2,fs2:'*2 + 'p.3.g2:'
pattern += ('p.3.c:p.3.g2:')*2
pattern += 'p.2.b2,a2:p.3.b2:'
pattern += 'p.2.e,d:p.2.e,a2:'
pattern += 'p.2.b2,a2:p.1.b2:b2.1.1:c.1.1:d.1.1:'
pattern += 'e.7.:d.1.:e.7.:a2.1.:b2.7.:a2.1.:b2.3.:b2.1.:b2.1.1:c.1.1:d.1.1:'

# E
pattern += 'p.3.e2:'*2
pattern += 'p.2.g2,a2:p.1.b2:b2.1.1:c.1.1:d.1.1:'
pattern += 'p.3.e2:'*2
pattern += ('p.2.b2,a2:'*2 + 'p.2.b2,c:p.1.d:d.1.1:c.1.1:a2.1.1:') * 2
##

# F
pattern += 'p.2.g2,fs2:' * 3 + 'p.3.g2:'
pattern += 'p.3.d2:p.2.g2,fs2:p.2.g2,fs2:p.3.g2:'
pattern += 'p.3.c:p.3.g2:' * 2
pattern += 'p.2.b2,a2:p.3.b2:'
pattern += 'p.2.e,d:' * 2 + 'p.2.e,fs:g.3.:g.1.:g.1.1:fs.1.1:d.1.1:'
pattern += 'e.7.:d.1.:'*2 + 'e.7.:fs.1.:p.1.g:p.1.fs:e2.20.:e2.12.:'
pattern += 'END'

point = 0

def get_note(phrase):
    note, phrase = phrase.split(':', 1)
    pt, ln, tp = note.split('.')
    return pt, ln, tp, phrase

play = True
hz = None
phrase = ''
tick = 3
tick_t = types['']
t = -1
pulse = 0
while play:
    while pin1.read_digital() == pulse:
        pass
    pulse = 1 - pulse
    t += 1

    if t >= point:
        stop()
        if phrase:
            pt, ln, tp, phrase = get_note(phrase)
            hz = notes[pt]
            point += int(ln) * types[tp]
        elif pattern != 'END':
            pt, ln, tp, pattern = get_note(pattern)
            if pt == 'p':
                phrase = patterns[int(ln)]((tp.split(',')))
                pt, ln, tp, phrase = get_note(phrase)
            hz = notes[pt]
            point += int(ln) * types[tp]
        else:
            play = False
    else:
        if hz != None:
            pitch(hz)

    #if t > tick_t:
    #    display.set_pixel(tick, 0, 0)
    #    tick = (tick + 1) % 4
    #    display.set_pixel(tick, 0, 8)
    #    tick_t += types[''] * 4

stop()
