from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# shift = 20
#
# for index in range(0,3):
#     turtle = Turtle(shape="square")
#     turtle.color("white")
#     new_xcor = turtle.xcor() - index*shift
#     turtle.goto(x=new_xcor,y=0)

# starting_positions = [(0,0), (-20,0), (-40,0)] #List of tuples for coordinates

# segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()


    #Detect collisions with food
    if snake.head.distance(food) < 15:
        print("Collided")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Detech collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        scoreboard.game_over()

    #Detech collision with tail
    #If head collides with any segment in the tail

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 15:
    #         game_is_on = False
    #         scoreboard.game_over()


    #Implemented the same as above but using the concept of slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()




# #below syntax is range(start,stop,step)
#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)


screen.exitonclick()
