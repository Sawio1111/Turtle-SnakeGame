from turtle import Turtle

snake_tail_start = [(0,0), (-20, 0), (-40, 0)]
snake_move_distance = 20


class Snake():
	def __init__(self):
		self.snake_tail = []
		self.creates_snake()
		self.snake_head = self.snake_tail[0]

	def creates_snake(self):
		for element in snake_tail_start:
			self.add_element_snake(element)

	def add_element_snake(self, position):
		snake = Turtle("square")
		snake.color("white")
		snake.penup()
		snake.goto(position)
		self.snake_tail.append(snake)

	def extend_snake(self):
		self.add_element_snake(self.snake_tail[-1].position())

	def move_snake(self):
		for element_number in range(len(self.snake_tail) - 1, 0, -1):
			new_x = self.snake_tail[element_number - 1].xcor()
			new_y = self.snake_tail[element_number - 1].ycor()
			self.snake_tail[element_number].goto(new_x, new_y)
		self.snake_head.forward(snake_move_distance)

	def up(self):
		if self.snake_head.heading() != 270:
			self.snake_head.setheading(90)

	def down(self):
		if self.snake_head.heading() != 90:
			self.snake_head.setheading(270)

	def left(self):
		if self.snake_head.heading() != 0:
			self.snake_head.setheading(180)

	def right(self):
		if self.snake_head.heading() != 180:
			self.snake_head.setheading(0)