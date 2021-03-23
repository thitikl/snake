from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setup screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

#call snake, food and scoreboard class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#setup control of snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
  screen.update()
  time.sleep(0.2)
  snake.move()
  
  #detect food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.add_score()
    scoreboard.show_score()
  
  #detect border  
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_on = False
    scoreboard.game_over()
  
  #detect self-intersect  
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_on = False
      scoreboard.game_over()