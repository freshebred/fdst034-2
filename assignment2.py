import turtle
screen = turtle.Screen()
screen.setup(1000,1000)

# This will be the player
player = turtle.Turtle()
player.color("black")
player.speed(0)
player.pensize(3)

# This pen draws the death zone
die = turtle.Turtle()
die.hideturtle()
die.color("#FFCCCB","#FFCCCB")
die.speed(0)


# This pen draws the menus
menu = turtle.Turtle()
menu.hideturtle()
menu.speed(0)


# This pen create interaction wrappers.
interact = turtle.Turtle()
interact.hideturtle()
interact.speed(0)

# This pen will draw monsters
# (Only if we ever decide to have monsters that would be a lot of work btw)
monster = turtle.Turtle()
monster.hideturtle()
monster.speed(0)



"""
-----------------------1. Essential functions---------------------
"""
# Draw rectangles
def draw_rect(p, h, w):
    p.setheading(90)
    for i in range(2):
        p.forward(h)
        p.right(90)
        p.forward(w)
        p.right(90)

# moves to a position
def p_move(p, x, y):
    p.up()
    p.goto(x,y)
    p.down()

# Fills color
def color_fill(p, outline, fill):
    if outline:
        p.color(outline)
    if fill:
        p.fillcolor(fill)
        p.begin_fill()

# Saves player location to memory
def record(x,y):
    x=round(x)
    y=round(y)
    h.append([x,y])
"""
-----------------------2. Set up here---------------------
"""
# History moves so the players cannot overlap themself
h=[]

# blocks of wall
dead_zone=[]

# Win tile
win_tile=[]

# Master function to start the game, with l being the level
def init(l):
    # Draws the start point
    p_move(interact, -500, -500)
    color_fill(interact, "black", "#8B8B8B")
    draw_rect(interact, 100, 100)
    interact.end_fill()

    # Draw the finish box
    win_zone(interact, 400,400,500,500)
    interact.end_fill()

    # Move player to initial position
    p_move(player, -450, -450)

    # Done, passing off to -> Initialize keystroke binding
    init_obstacle(l)
    init_player()
    if l == 0:
        main_screen_show()

"""That's crazy
-----------------------3. Framework logics below here (All, we'll make this progressively)---------------------

"""
def deadzone(p, x1, y1, x2, y2):
    # check if the coordinate is valid:
    if x1>x2 or y1>y2:
        raise ValueError("Coordinate for dead zone x1 or y1 must be lower than or equal to x2 or y2!")
    for v in [x1,x2,y1,y2]:
        if v<-500 or v>500:
            raise ValueError("Coordinates for dead zone must be in the range -500 to 500px")
    p_move(p, x1, y1)
    color_fill(p, "#FF474C", "#FF474C")
    draw_rect(p, y2-y1,x2-x1)
    p.end_fill()
    dead_zone.append([x1, y1, x2, y2])

def win_zone(p, x1, y1, x2, y2):
    if x1>x2 or y1>y2:
        raise ValueError("Coordinate for win zone x1 or y1 must be lower than or equal to x2 or y2!")
    for v in [x1,x2,y1,y2]:
        if v<-500 or v>500:
            raise ValueError("Coordinates for win zone must be in the range -500 to 500px")
    p_move(p, x1, y1)
    color_fill(p, "#8FFF72", "#8FFF72")
    draw_rect(p, y2-y1,x2-x1)
    global win_tile
    win_tile = [x1, y1, x2, y2]

# This goes in pair! if you call validate and it gives something else than 0, call dictionary to know what it means.
# Example:
# 
# valid = validate()                      # 2
# if valid != 0:                          # True
#     text = dictionary(valid)            # "You hit a wall"
#     game_over(text)                     #  Display the text "You hit a wall"

def dictionary(c):
    codes = ["Good", "You overlapped yourself", "You hit a wall", "You ran out of bound", "You won"]
    return codes[c]
def validate():
    x = round(player.xcor())
    y = round(player.ycor())
    for zone in dead_zone:
        if zone[0] <= x <= zone[2] and zone[1] <= y <= zone[3]:
            return 2
    if win_tile and win_tile[0] <= x <= win_tile[2] and win_tile[1] <= y <= win_tile[3]:
        return 4
    if h.__contains__([x,y]):
        return 1
    elif (-500>x or 500<x) or (-500>y or 500<y):
        return 3
    else:
        return 0




def framework():
    pass

"""
-----------------------4. Player logic below here (Thashith)---------------------
"""

# Make the player move forward(10) in that direction
# Make sure to call the function validate() at the end of the function
def move_w():
    # Example:
    # Step 1: Record current position of the player
    record(player.xcor(), player.ycor())

    # Step 2: make the player go in the direction they moved
    player.setheading(90)
    player.forward(10)

    # Step 3: check if the position they moved to wins or loses or nothing
    # When running validate(), it will return a code of 0-4, check the function dictionary(c) to know what each code means
    result = validate()
    
    # validate() return 4 means the user reached the end, and they won
    if result == 4:
        you_win()
    # validate() return 0 means the player made a VALID move, therefore, ANY result OTHER than 0 means the player lost.
    elif result != 0:
        game_over(dictionary(result))


def move_s():
    pass
def move_a():
    pass
def move_d():
    pass

def init_player():
    # Write player logics here and also define key events here too
    keys=["w","a","s","d","Up","Left","Down","Right"]

"""
-----------------------5. Draw levels and death block logic below here (Thashith)---------------------
"""


def init_obstacle(level):
    match level:
        case 0:
            # Write code for level 1
            pass
        case 1:
            # write code for level 2
            pass
        case 2:
            # Write code for level 3
            pass
        case _:
            raise ValueError("Level must be 0-2")


"""
-----------------------6. Menu designs below here (Meg)---------------------
"""

# Stores a list of buttons. the syntax for appending button coordinates are [x1,y1,x2,y2]
buttons = []
action = None


# Function to show the main screen and hide the main screen (main screen is the screen to say like welcome to our game, made by who, ...)
# Remember! You need to remove the button wrapper when you hide a screen!
def main_screen_show():
    global buttons, action
    menu.up()
    p_move(menu, -400, -400)
    color_fill(menu, False, "gray")
    draw_rect(menu, 800, 800)
    menu.end_fill()
    p_move(menu, -200, -20)
    menu.write("Hi welcome to our game, click to start", font=("Arial", 24, "normal"))
    p_move(menu, -200, -300)
    color_fill(menu, False, "green")
    draw_rect(menu, 400, 100)
    menu.end_fill()
    p_move(menu, -100, -250)
    menu.write("Start", font=("Arial", 24, "normal"))

    # Flat list of coordinates: [x1, y1, x2, y2]
    buttons = [-200, -300, 200, -200]
    action = menu_screen_clear


def menu_screen_clear():
    global buttons, action
    buttons = []
    action = None
    menu.clear()
    pass


# Function to show the you lost screen
def game_over(text):
    stop_game()
    pass


def you_win():
    pass


def button_clicked(cor):
    pass


def click(x, y):
    x = round(x)
    y = round(y)
    # Check if button does exist first, then check if the user clicked on it
    if len(buttons) == 4 and buttons[0] <= x <= buttons[2] and buttons[1] <= y <= buttons[3]:
        # Caught that the user clicked a button and execute action
        if action is not None:
            action()
"""
-----------------------7. Configuratiion stuffs here (Nam)-------------------
"""

def reset_all():
    player.clear()
    menu.clear()
    die.clear()
    interact.clear()
    h.clear()
    dead_zone.clear()
    win_tile.clear()
    init(0)

def reset_playfield():
    player.clear()
    menu.clear()
    die.clear()
    interact.clear()
    h.clear()
    dead_zone.clear()
    win_tile.clear()

def stop_game():
    # unbind all keys
    keys=["w","a","s","d","Up","Left","Down","Right"]
    for key in keys:
        screen.onkeypress(None, key)

screen.onkey(reset_all, "r")


# Start everything
init(0)

screen.listen()
screen.mainloop()