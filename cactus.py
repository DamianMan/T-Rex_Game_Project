from turtle import Turtle


class Cactus(Turtle):
    def __init__(self,pos):
        super(Cactus, self).__init__()
        self.hideturtle()
        self.shape('cactus.gif')

        self.pu()
        self.goto(pos)
        self.showturtle()
        self.x_move = 10
        self.new_x = 0


    def move(self):
        self.new_x = self.xcor() - self.x_move
        self.goto(self.new_x, self.ycor())

    def restart(self, x, y):
        self.goto(x,y)

