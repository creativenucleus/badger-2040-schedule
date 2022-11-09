import badger2040

badger = badger2040.Badger2040()
badger.update_speed(badger2040.UPDATE_NORMAL)

WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT
TEXTAREA_WIDTH = 196

from cn_schedule.config import event_title, sessions

sessionId = 0
N_SESSIONS = len(sessions)

PROGRESS_HEIGHT = 10

for session in sessions:
    session['image_data'] = bytearray(int(96 * 96 / 8))
    open("cn_schedule/images/" + session['image_src'], "r").readinto(session['image_data'])

def split_text(text, maxWidth, scale):
    lines = []
    
    words = text.split()
    
    buildLine = ""
    tryLine = ""
    while words:
        nextWord = words.pop(0)
        if buildLine:
            tryLine = buildLine + " "
        tryLine = tryLine + nextWord
        textWidth = badger.measure_text(tryLine, scale)
        if textWidth <= maxWidth:
            buildLine = tryLine
        else:
            lines.append(buildLine)
            buildLine = nextWord
            
   # If there's still something in the buffer then flush it...
    if buildLine:
        lines.append(buildLine)
    
    return lines

def text_scale(text, maxWidth, maxScale):
    steps = 20
    for tryStep in range(steps, 1, -1):
        scale = (tryStep / steps) * maxScale
        textWidth = badger.measure_text(text, scale)
        if textWidth <= maxWidth:
            return scale
    return scale

def draw_text():    
    badger.pen(0)
    badger.thickness(1)
    
    session = sessions[sessionId]
    
    badger.font("bitmap8") # "sans", "bitmap8", "bitmap14_outline"

    time = "{0}  ~  {3} ({1}-{2})".format(event_title, session['start'], session['end'], session['title'])
    textWidth = badger.measure_text(time, 1.0)
    badger.text(time, int((WIDTH - textWidth)/2), 0, 1.0)
#    badger.text(time, 0, 0, 1.0)

    badger.font("sans") # "sans", "bitmap8", "bitmap14_outline"
    scale = text_scale(session['speaker'], TEXTAREA_WIDTH, 1.0)
    badger.text(session['speaker'], 0, int(22 + scale * 5), scale)

    scale = text_scale(session['sub'], TEXTAREA_WIDTH, 1.0)
    badger.text(session['sub'], 0, int(43 + scale * 5), scale)

    badger.font("bitmap6") # "sans", "bitmap8", "bitmap14_outline"
    lines = split_text(session['description'], TEXTAREA_WIDTH, 1.0)
    for i, line in enumerate(lines):
        if i < 5:
            badger.text(line, 0, 63 + i * 10, 1.0)
        
def draw_progress():
    for x in range(N_SESSIONS):
        x0 = (WIDTH * x) / (N_SESSIONS)
        x1 = ((WIDTH * (x + 1)) / (N_SESSIONS)) - 2
        
        if x <= sessionId:
            badger.pen(4)
        else:
            badger.pen(12)
    
        badger.rectangle(int(x0), HEIGHT - PROGRESS_HEIGHT, int(x1) - int(x0), PROGRESS_HEIGHT)

def draw_screen():
    badger.pen(15)
    badger.clear()

    badger.image(sessions[sessionId]['image_data'], 96, 96, WIDTH - 96, 15)
    draw_text()
    draw_progress()
    badger.update()

draw_screen()

while True:
    if badger.pressed(badger2040.BUTTON_UP) and sessionId > 0:
        sessionId -= 1
        draw_screen()
    elif badger.pressed(badger2040.BUTTON_DOWN) and sessionId < N_SESSIONS - 1:
        sessionId += 1
        draw_screen()