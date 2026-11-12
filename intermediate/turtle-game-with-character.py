# Find or create a character image.
# Save it in GIF format.
# Name it player.gif.
# Keep the image in the same folder as your Python program.

import turtle

# Create screen
screen = turtle.Screen()
screen.title("My Custom Character Game")
screen.bgcolor("lightblue")

# Load custom character
screen.register_shape("player.gif")

# Create player
player = turtle.Turtle()
player.shape("player.gif")
player.penup()

# Movement functions
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

# Keyboard controls
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(close_game, "q")

# Start game
turtle.done()
