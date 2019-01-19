key_pressed = [False for key_code in range(256)]
bird_pos = [200, 240]
x_pipe = 640
pipe_width = 60
diameter = 50
counter = 0
pipe_endpoint = x_pipe + pipe_width
import random


def setup():
    size(640, 480)

def draw_pipes():
    #pipes/jail bars
    global x_pipe
    top_pipe_height = random.randint (50, 281)
    pipe_gap = 150
    pipe_width = 60
    bottom_pipe_height = heihgt - top_pipe_height - pipe_gap
    bottom_pipe_pipe = pipe_height + pipe_gap
    fill (0, 255, 0)
    if x_pipe >= -60:
        x_pipe -= 5
    rect (x_pipe, -1, pipe_width, randnum)
    rect (x_pipe, randnum + pipe_gap, pipe_width, height - randnum - pipe_gap)

# game_on = True
# while game_on == True:
# if bird_pos[0] >= x_pipe - diameter and bird_pos[0] <= x_pipe + pipe_width + diameter and bird_pos[1] <= randnum + diameter or bird_pos[0] >= randnum_pipe_gap + diameter:
#     game_on == False
# constrain(x_bird, x_pipe, pipe_endpoint)

def constrain(x_bird, x_pipe, pipe_endpoint):
    if x_bird < x_pipe: print x_pipe
    if x_bird > pipe_endpoint: print pipe_endpoint
    print x_bird

def draw():
    background(211)
    global x_pipe
    global bird_pos
    global pipe_width
    global pipe_endpoint
    global diameter
    global counter
    
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
    
    #bird and bird movement
    fill (255, 255, 100)
    stroke (0)
    ellipse (bird_pos[0], bird_pos[1], diameter, diameter)
    
    if bird_pos[1] != height:
        bird_pos[1] += 1
    elif bird_pos[1] > height:
        bird_pos[1] = height
    
    if key_pressed [38] and bird_pos[1] >= 0:
        bird_pos[1] -= 4
    if key_pressed [40] and bird_pos[1] != height:
        bird_pos[1] += 4
    if key_pressed [37] and bird_pos[0] >= 0:
        bird_pos[0] -= 4
    if key_pressed [39] and bird_pos[0] <= width:
        bird_pos[0] += 4
        
    #pipes 
    counter += 1
    if counter % 4 == 0:
         draw_pipes()
        
def keyPressed():
    global key_pressed
    key_pressed[keyCode] = True 
    
def keyReleased():
    global key_pressed
    key_pressed[keyCode] = False
