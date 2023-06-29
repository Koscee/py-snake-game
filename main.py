from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

BOUNDARY = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create snake
snake = Snake()
# create food
food = Food()
# initialize score board
score_board = ScoreBoard()

# listen to key events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def hit_wall():
    return snake.head.xcor() > BOUNDARY \
           or snake.head.xcor() < -BOUNDARY \
           or snake.head.ycor() > BOUNDARY \
           or snake.head.ycor() < -BOUNDARY

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()

    # detect collision with wall
    if hit_wall():
        game_is_on = False
        score_board.game_over()

screen.exitonclick()
