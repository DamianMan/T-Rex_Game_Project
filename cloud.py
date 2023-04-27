from turtle import Turtle


class Cloud(Turtle):
    def __init__(self,pos):
        super(Cloud, self).__init__()
        self.hideturtle()
        self.shape('cloud.gif')

        self.pu()
        self.goto(pos)
        self.showturtle()
        self.x_move = 6
        self.new_x = 0


    def move(self):
        self.new_x = self.xcor() - self.x_move
        self.goto(self.new_x, self.ycor())

    def restart(self, x, y):
        self.goto(x,y)