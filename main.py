import turtle

image = "board.gif"

# Design the board
screen = turtle.Screen()
screen.title("Tic-Tac-Toe")
screen.addshape(image)
turtle.shape(image)

# Design players
x_image = "player_X.gif"
o_image = "player_O.gif"
x = turtle.Turtle()
# x.hideturtle()
screen.addshape(x_image)
x.shape(x_image)
o = turtle.Turtle()
# o.hideturtle()
screen.addshape(o_image)
o.shape(o_image)

while True:
# Select Player
    user_answer = screen.textinput("Select Avatar", "Choose your avatar: X or O:").lower()
    if user_answer == x:
        x.setpos(0,0)
    else:
        o.setpos(100,100)

#todo 1: Get white background image for x and o
#todo 2: Get turtle method for reducing image size and reduce sizes of x and o to fit box
#todo 3: Get the code block for getting x and y coordinate from mouse click
#todo 4: create scoreboard


# screen.exitonclick()