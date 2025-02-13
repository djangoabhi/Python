from turtle import Turtle
import random

#Inhertitance below
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-260,260)
        random_y = random.randint(-260,260)
        self.goto(random_x, random_y)


    def refresh(self):
        random_x = random.randint(-260,260)
        random_y = random.randint(-260,260)
        self.goto(random_x, random_y)