from turtle import Screen, Turtle
from turtle_behave import Turtles  # Importing custom turtle behavior class

# Initialize the screen
screen = Screen()
screen_height = 400
screen_width = 500

# Function to draw the finish line
def draw_finish_line():
    judge = Turtle()
    judge.hideturtle()
    judge.penup()
    judge.goto(150, 190)
    judge.right(90)
    judge.pendown()
    judge.forward(190 * 2)

# Draw the finish line
draw_finish_line()

# Set up the screen dimensions
screen.setup(width=screen_width, height=screen_height)

# Set the title and prompt for user interaction
title = 'Make your bet'
prompt = 'Which turtle will win the race:\n colors from red, green, blue, yellow, purple, orange'
user_bet = screen.textinput(title=title, prompt=prompt)

# Define turtle colors and number of turtles
colors = ["red", "orange", "yellow", "green", 'blue', 'purple']
num_turtles = len(colors)

# Calculate starting positions for each turtle
turtle_spread_over_y_direction = screen_height / 2
first_turtle_starting_position_y = -turtle_spread_over_y_direction + (turtle_spread_over_y_direction / 2)
y_gap_turtles = turtle_spread_over_y_direction / (num_turtles - 1)
starting_y_positions = [first_turtle_starting_position_y + i * y_gap_turtles for i in range(num_turtles)]

# Create turtle instances and set up their positions and colors
turtle_list = [Turtles('t1'), Turtles('t2'), Turtles('t3'), Turtles('t4'), Turtles('t5'), Turtles('t6')]
for turtle_ in turtle_list:
    turtle_.setup(colors[turtle_list.index(turtle_)])
    turtle_.goto_start_position(starting_y_positions[turtle_list.index(turtle_)])

# Determine the winning turtle's color and position
win_color = ''
while len(win_color) == 0:
    for turtle_ in turtle_list:
        turtle_.random_run()
        if turtle_.current_position() > 200:
            win_color = colors[turtle_list.index(turtle_)]
            turtle_position = turtle_list[turtle_list.index(turtle_)].current_position()
            print(win_color)
            print(turtle_position)

# Check if user's bet matches the winning turtle's color
if user_bet == win_color:
    print('Congratulations! You won!')
else:
    print('Sorry, you lost!')

# Wait for user click to exit the screen
screen.exitonclick()

