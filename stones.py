from turtle import Turtle


class Stones(Turtle):
    def __init__(self, pos):
        super(Stones, self).__init__()
        self.pu()
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_wid=0.05,stretch_len=0.3)
        self.goto((pos))
        self.x_move = 10
        self.new_x = 0
        self.new_y = 0

    def move(self):
        self.showturtle()
        self.new_x = self.xcor() - self.x_move
        self.goto(self.new_x, self.ycor())

    def restart(self, position_x, position_y):

        self.goto(position_x, position_y)