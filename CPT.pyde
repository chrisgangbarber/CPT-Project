key_pressed = [False for key_code in range(256)]
y_bird = 240
x_bird = 200
x_pipe = 640
pipe_width = 60
pipe_endpoint = x_pipe + pipe_width
import random
randnum = random.randint (50, 281)

def setup():
    size(640, 480)

# def draw_pipes():
#     #pipes/jail bars
#     global x_pipe
#     global randnum
#     fill (0, 255, 0)
#     if x_pipe >= -60:
#         x_pipe -= 5
#     pipe_gap = 150
#     pipe_width = 60
#     rect (x_pipe, -1, pipe_width, randnum)
#     rect (x_pipe, randnum + pipe_gap, pipe_width, height - randnum - pipe_gap)

# game_on = True
# if game_on == True:
#     draw_pipes()


def constrain(x_bird, x_pipe, pipe_endpoint):
    if x_bird < x_pipe: print x_pipe
    if x_bird > pipe_endpoint: print pipe_endpoint
    print x_bird

def draw():
    background(211)
    global y_bird
    global x_pipe
    global pipe_width
    global x_bird
    global pipe_endpoint
    
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
    
    #pipes
    fill (0, 255, 0)
    if x_pipe >= -60:
        x_pipe -= 5
    pipe_gap = 110
    
    rect (x_pipe, -1, pipe_width, randnum)
    rect (x_pipe, randnum + pipe_gap, pipe_width, height - randnum - pipe_gap)
    
    constrain(x_bird, x_pipe, pipe_endpoint)
        
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
        

        
    
