from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Move:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.color("brown")
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            x_aixs = self.segments[seg_no - 1].xcor()
            y_aixs = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(x_aixs, y_aixs)

        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(-180)
