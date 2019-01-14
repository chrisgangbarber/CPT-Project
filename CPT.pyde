key_pressed = [False for key_code in range(256)]
y_bird = 240
x_bird = 200
x_pipe = 640
import random
randnum = random.randint (50, 281)

def setup():
    size(640, 480)

def draw():
    background(211)
    global y_bird
    global x_pipe
    global x_bird
    
    #doors
    noStroke ()
    fill (210, 180, 140)
    for k in range (100, 500, 250):
        rect (k, 200, 150, 300)
    fill (248, 248, 255)
    rect (430, 230, 40, 90)
    rect (180, 230, 40, 90)
    fill (255, 255, 0)
    for i in range (235, 500, 250):
        ellipse (i, 330, 15, 15)

    #second floor of jail
    fill (245,245,220)
    rect(0, height - 50, width, 50)
    
    #railing
    for i in range (350, 420, 25):
        rect (0, i, width, 10)
    for j in range (40, 640, 80):
        rect (j, 360, 5, 80)
    
    #bird jump
    fill (255, 255, 100)
    stroke (0)
    ellipse (x_bird, y_bird, 50, 50)
    
    if y_bird != height:
        y_bird += 1
        
    #pipes/jail bars
    fill (0, 255, 0)
    if x_pipe >= -60:
        x_pipe -= 5
    global randnum
    pipe_gap = 150
    rect (x_pipe, -1, 60, randnum)
    rect (x_pipe, randnum + pipe_gap, 60, height - randnum - pipe_gap)
    
    if x_pipe <= 540:
        rect (640, -1, 60, randnum)
        rect (640, randnum + pipe_gap, 60, height - randnum - pipe_gap)
    
    #bird movement
    if key_pressed [38]:
        y_bird -= 4
    if key_pressed [40]:
        y_bird += 4
    if key_pressed [37]:
        x_bird -= 4
    if key_pressed [39]:
        x_bird += 4

def keyPressed():
    global key_pressed
    key_pressed[keyCode] = True 
    
def keyReleased():
    global key_pressed
    key_pressed[keyCode] = False
        

        
    
