from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 32, "normal"))







