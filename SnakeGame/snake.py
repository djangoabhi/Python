from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] #List of tuples for coordinates
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())


    def move(self):
        # below syntax is range(start,stop,step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # pass
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # pass
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # pass
        if self.head.heading() != 180:
            self.head.setheading(0)




