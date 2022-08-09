from turtle import Turtle


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.goto(0, 270)
		self.color("white")
		self.penup()
		self.hideturtle()
		self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "normal"))
		self.speed("fastest")


	def increase_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "normal"))

	def game_over(self):
		self.goto(0, 0)
		self.write(f"Game over", False, "center", ("Arial", 50, "normal"))