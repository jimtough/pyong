from turtle import Turtle

STARTING_MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # ball will get a little faster each time it hits a paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # reverse direction this time
        self.bounce_x()
        self.move_speed = STARTING_MOVE_SPEED
