# Sir before you start, you need to add the three png files that are in the master branch to your processing program. 
# Download the pictures then click on sketch at the top and add the three pictues by clicking add files

import random
key_pressed = [False for key_code in range(256)]
player_pos = [200, 240]
x_pipe = 640
diameter = 50
counter = 0
x_start = 700
pipe_width = 60
pipe_endpoint = x_pipe + pipe_width
speed = 4
score = 0
pipe_gap = 175
timer = 0
theta = 0
game_over = False
start_game = False

pipe_x_pos = []
top_pipe_bottom = []
bottom_pipe_top = []

# initial values of pipes
pipe_x_pos.append(500)
top_pipe_bottom.append(100)
bottom_pipe_top.append(250)


def setup():
    size(640, 480)
    imageMode(CENTER)


def game_background():
    # doors
    noStroke()
    fill(210, 180, 140)
    for k in range(100, 500, 250):
        rect(k, 200, 150, 300)
    fill(248, 248, 255)
    rect(430, 230, 40, 90)
    rect(180, 230, 40, 90)
    fill(255, 255, 0)
    for i in range(235, 500, 250):
        ellipse(i, 330, 15, 15)

    # second floor of jail
    fill(245, 245, 220)
    rect(0, height - 50, width, 50)

    # railing
    for i in range(350, 420, 25):
        rect(0, i, width, 10)
    for j in range(40, 640, 80):
        rect(j, 360, 5, 80)


def random_pipe():
    global x_start
    global speed
    global pipe_gap
    top_pipe_bottom_pos = random.randint(50, 300)
    bottom_pipe_top_pos = top_pipe_bottom_pos + pipe_gap
    pipe_x_pos.append(x_start)
    top_pipe_bottom.append(top_pipe_bottom_pos)
    bottom_pipe_top.append(bottom_pipe_top_pos)


def start_screen():
    global start_game
    background(255)
    fill(0)
    img_69Court = loadImage("69 court.png")
    image(img_69Court, width // 2, 240, 140, 140)
    textAlign(CENTER)
    textSize(50)
    text("6ix9ine is locked up!", 320, 100)
    text("Help him survive jail!", 320, 150)
    textSize(25)
    text("Press UP ARROW to commence the escape", 320, 400)
    text("Avoid the jail bars", 320, 450)
    text("Use arrow keys to move", 320, 350)

    if key_pressed[38]:
        start_game = True


def game_over_screen():
    message = "FAIL!"
    global font
    global theta
    global img_prisoner
    global img_prisonGuard
    size(640, 480)
    font = createFont("Atlas", 60, True)
    img_prisonGuard = loadImage("prison guard.png")
    background(255, 38, 0)
    image(img_prisonGuard, width // 2, 240)
    fill(255)
    textFont(font)
    translate(width/2, height/2)
    rotate(theta)
    textAlign(CENTER)
    text(message, 0, 0)
    theta += 0.01


def draw():
    background(211)
    global player_pos
    global pipe_width
    global diameter
    global counter
    global pipe_x_pos
    global top_pipe_bottom
    global bottom_pipe_top
    global speed
    global score
    global pipe_gap
    global timer
    global game_over
    global start_game

    game_background()

    if start_game is False:
        start_screen()
    elif start_game is True:
        # player and player movement
        fill(255, 255, 100)
        stroke(0)
        ellipse(player_pos[0], player_pos[1], diameter, diameter)
        img_69Ellipse = loadImage("69 final form.png")
        image(img_69Ellipse, player_pos[0], player_pos[1], 50, 50)
        if player_pos[1] != height:
            player_pos[1] += 1
        elif player_pos[1] > height:
            player_pos[1] = height

        if key_pressed[38] and player_pos[1] >= 0:
            player_pos[1] -= 5
        if key_pressed[40] and player_pos[1] != height:
            player_pos[1] += 4
        if key_pressed[37] and player_pos[0] >= 0:
            player_pos[0] -= 4
        if key_pressed[39] and player_pos[0] <= width:
            player_pos[0] += 4

        # pipe movement
        if speed < 8:
            speed += 0.004
        else:
            speed = 8
        for i in range(0, len(pipe_x_pos)):
            pipe_x_pos[i] -= speed

        for j in range(0, len(pipe_x_pos)):
            fill(169)
            rect(pipe_x_pos[j], 0, pipe_width, top_pipe_bottom[j])
            rect(pipe_x_pos[j], bottom_pipe_top[j], pipe_width,
                 480 - bottom_pipe_top[j])

        if pipe_x_pos[0] < -60:
            pipe_x_pos.pop(0)
            top_pipe_bottom.pop(0)
            bottom_pipe_top.pop(0)

            random_pipe()
            fill(169)
            rect(pipe_x_pos[0], 0, pipe_width, top_pipe_bottom[0])
            rect(pipe_x_pos[0], bottom_pipe_top[0], pipe_width,
                 480 - bottom_pipe_top[0])

        if pipe_x_pos[len(pipe_x_pos)-1] < 300 and len(pipe_x_pos) <= 2:
            random_pipe()
            fill(169)
            rect(pipe_x_pos[len(pipe_x_pos)-1], 0,
                 pipe_width, top_pipe_bottom[len(top_pipe_bottom)-1])
            rect(pipe_x_pos[len(pipe_x_pos)-1],
                 bottom_pipe_top[len(bottom_pipe_top)-1],
                 pipe_width, 480 - bottom_pipe_top[len(bottom_pipe_top)-1])

        radius = diameter // 2

        # collision detection
        if (player_pos[0] >= pipe_x_pos[0] - radius + 5 and
            player_pos[0] <= pipe_x_pos[0] + pipe_width + radius - 5 and
            (player_pos[1] <= top_pipe_bottom[0] + radius - 5 or
             player_pos[1] >= top_pipe_bottom[0] + pipe_gap - diameter + 5) or
            (len(pipe_x_pos) > 1 and len(top_pipe_bottom) > 1 and
             player_pos[0] >= pipe_x_pos[1] - radius + 5 and
             player_pos[0] <= pipe_x_pos[1] + pipe_width + radius - 5 and
            (player_pos[1] <= top_pipe_bottom[1] + radius - 5 or
             player_pos[1] >= top_pipe_bottom[1] + pipe_gap - radius + 5))):
                game_over = True

        elif frameCount % 60 == 0:
            timer += 1

        stroke(10)
        fill(255, 255, 255)
        rect(370, 0, 300, 50)
        textSize(30)
        fill(0, 0, 0)
        text("Time survived: " + str(int(timer)) + "s", 360, 10, 300, 100)

    if game_over is True:
        game_over_screen()


def keyPressed():
    global key_pressed
    key_pressed[keyCode] = True


def keyReleased():
    global key_pressed
    key_pressed[keyCode] = False
