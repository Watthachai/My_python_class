from turtle import Turtle , Screen


tim = Turtle()
tim.shape("turtle")
tim.color("blue")

def draw_rectangle():
	for i in range(4):
		tim.fd(100)
		tim.left(90)

draw_rectangle()

my_screen = Screen()
my_screen.exitonclick()

