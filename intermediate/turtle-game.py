
import turtle

# Step 1: Create the screen
screen = turtle.Screen()
screen.title("Control the Turtle")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Step 2: Create the turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.speed(3)

# Step 3: Create movement functions
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

def close_game():
    screen.bye()
  
# Step 4: Listen to keyboard keys
screen.listen()

screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(close_game, "q")

# Step 5: Keep the window open
turtle.done()
