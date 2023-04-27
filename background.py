from turtle import Turtle


class Background(Turtle):
    def __init__(self,pos):
        super(Background, self).__init__()
        self.hideturtle()
        self.pu()
        self.goto(pos)
        self.left(180)
        self.pd()