import random
from turtle import Turtle

class Turtles:
    def __init__(self, name):
        # Initialize the turtle with its name and initial distance covered
        self.name = name
        self.current_distance = 0

    def setup(self, colour):
        # Set up the turtle's attributes such as shape, color, and penup status
        self.name = Turtle(shape='turtle')
        self.name.color(colour)
        self.name.penup()

    def goto_start_position(self, starting_pos):
        # Move the turtle to the starting position on the screen
        self.name.goto(x=-230, y=starting_pos)

    def random_run(self):
        # Generate a random distance for the turtle to move forward
        rand_position = random.randint(0, 10)
        self.name.forward(rand_position)
        return rand_position

    def current_position(self):
        # Update the current distance covered by the turtle and return it
        self.current_distance += self.random_run()
        return self.current_distance

    def stop_run(self):
        # Stop the turtle's movement by moving forward 0 units
        self.name.forward(0)










