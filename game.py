import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1000, 1000)

pen.speed(0)
die = turtle.Turtle()

h = []


def validate(x, y):
  # Checks if the user overlaps
  if [x, y] in h:
    pen.clear()
    die.clear()
    pen.up()
    pen.home()
    pen.down()
    pen.write("You overlapped yourself...")
    for key in ["Up", "Down", "Left", "Right", "w", "s", "a", "d"]:
      screen.onkeypress(None, key)


def move(o):
  match o:
    case "Up" | "w":
      pen.setheading(90)
    case "Down" | "s":
      pen.setheading(270)
    case "Right" | "d":
      pen.setheading(0)
    case "Left" | "a":
      pen.setheading(180)

  pen.forward(10)
  pos = [round(pen.xcor()), round(pen.ycor())]
  validate(pos[0], pos[1])
  h.append(pos)


die.hideturtle()
die.speed(0)


def dead(x1, y1, x2, y2, invis):
  if (
      x1 % 10 != 0
      or x2 % 10 != 0
      or y1 % 10 != 0
      or y2 % 10 != 0
      or x1 > x2
      or y1 > y2
  ):
    raise ValueError(
        "Dead zone coordinates must be divisible by 10, or x1/y1 must be"
        " smaller than x2/y2!"
    )

  if not invis:
    die.up()
    die.goto(x1, y1)
    die.down()
    die.fillcolor("#FFCCCB")
    die.begin_fill()
    die.goto(x1, y2)
    die.goto(x2, y2)
    die.goto(x2, y1)
    die.goto(x1, y1)
    die.end_fill()
    die.up()

  # Bottom edge (left to right)
  for x in range(x1, x2 + 1, 10):
    h.append([x, y1])

  # Right edge (bottom to top)
  for y in range(y1, y2 + 1, 10):
    h.append([x2, y])

  # Top edge (right to left)
  for x in range(x2, x1 - 1, -10):
    h.append([x, y2])

  # Left edge (top to bottom)
  for y in range(y2, y1 - 1, -10):
    h.append([x1, y])




def setup_game():
  dead(-500,-500,500,500,True)
  pen.up()
  pen.goto(-450, -450)
  pen.dot(50, "gray")
  pen.down()
  dead(-500, -400, 400, -300, False)


setup_game()
screen.onkeypress(lambda: move("w"), "Up")
screen.onkeypress(lambda: move("s"), "Down")
screen.onkeypress(lambda: move("a"), "Left")
screen.onkeypress(lambda: move("d"), "Right")

screen.onkeypress(lambda: move("w"), "w")
screen.onkeypress(lambda: move("s"), "s")
screen.onkeypress(lambda: move("a"), "a")
screen.onkeypress(lambda: move("d"), "d")

screen.listen()
screen.mainloop()