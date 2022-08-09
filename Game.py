from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_state = True

while game_state:
	screen.update()
	time.sleep(0.1)
	snake.move_snake()
	if snake.snake_head.distance(food) < 15:
		food.refresh()
		scoreboard.increase_score()
		snake.extend_snake()

	if snake.snake_head.xcor() > 280 or snake.snake_head.ycor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280:
		game_state = False
		scoreboard.game_over()

	for element in snake.snake_tail:
		if element == snake.snake_head:
			pass
		elif snake.snake_head.distance(element) < 10:
			game_state = False
			scoreboard.game_over()




screen.exitonclick()