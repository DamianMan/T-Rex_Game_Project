from turtle import Turtle


class T_rex(Turtle):
    def __init__(self):
        super(T_rex, self).__init__()
        self.hideturtle()
        self.shape('t-rex.gif')
        self.speed(0)

        self.pu()
        self.goto(-500, 0)
        self.showturtle()
        self.new_y = 0
        self.new_x = 0



    def jump(self):
        self.new_y = 8

















