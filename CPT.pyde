#key_pressed = [False for key_code in range(256)]
y_bird = 240
x_pipe = 640
import random
randnum = random.randint (50, 281)

def setup():
    size(640, 480)

def draw():
    background(211)
    global y_bird
    global x_pipe
    
    #doors
    noStroke ()
    fill (210,180,140)
    for k in range (100, 500, 250):
        rect (k, 200, 150, 300)

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
    ellipse (200, y_bird, 50, 50)
    
    if y_bird != height:
        y_bird += 2
        
    #pipes/jail bars/rectangles
    fill (0, 255, 0)
    if x_pipe >= -60:
        x_pipe -= 5
    global randnum
    pipe_gap = 150
    rect (x_pipe, -1, 60, randnum)
    rect (x_pipe, randnum + pipe_gap, 60, height - randnum - pipe_gap)

    

def keyPressed():
    global y_bird
    if keyCode == 38 and y_bird!= 0:
        y_bird -= 80
        

        
    
