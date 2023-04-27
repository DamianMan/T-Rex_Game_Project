import turtle
from turtle import Screen
from t_rex import T_rex
from background import Background
from stones import Stones
from cactus import Cactus
from cloud import Cloud
import sys
import os


screen = Screen()
screen.title('T-Rex Game')
screen.tracer(0)





GRAVITY = -0.3

def esc():
    sys.exit()

def play_again():
    os.execv(sys.executable, ['python'] + sys.argv)


turtle.register_shape('t-rex.gif')
t_rex = T_rex()


screen.listen()
screen.onkey(t_rex.jump, 'space')

turtle.register_shape('cactus.gif')
cactus = Cactus((1400, 0))
cactus1 = Cactus((2400, 0))
cactus2 = Cactus((2450, 0))
cactus3 = Cactus((3500, 0))
cactus4 = Cactus((3800, 0))
cactus5 = Cactus((5000, 0))






turtle.register_shape('cloud.gif')
cloud = Cloud((1000, 300))
cloud1 = Cloud((2000, 400))
cloud2 = Cloud((2100, 330))

# background
line = Background((650, -15))

stones = Stones((600, -30))
stones2 = Stones((690, -35))
stones3 = Stones((750, -40))
stones4 = Stones((900, -30))
stones5 = Stones((1080, -35))
stones6 = Stones((1200, -40))
stones7 = Stones((1400, -30))
stones8 = Stones((1550, -35))
stones9 = Stones((1750, -40))





def activate_game():
    # Stones restart
    if stones.xcor() < -650:
        screen.update()

        stones.restart(700, -25)
    if stones2.xcor() < -650:
        screen.update()
        stones2.restart(680, -30)
    if stones3.xcor() < -650:
        screen.update()
        stones3.restart(650, -35)
    if stones4.xcor() < -650:
        screen.update()
        stones4.restart(720, -25)
    if stones5.xcor() < -650:
        screen.update()
        stones5.restart(750, -30)
    if stones6.xcor() < -650:
        screen.update()
        stones6.restart(770, -35)
    if stones7.xcor() < -650:
        screen.update()
        stones7.restart(780, -25)
    if stones8.xcor() < -650:
        screen.update()
        stones8.restart(820, -30)
    if stones9.xcor() < -650:
        screen.update()

        stones9.restart(880, -35)

    # Cactus restart
    if cactus.xcor() < -700:
        cactus.restart(2000, 0)
    if cactus1.xcor() < -700:
        cactus1.restart(3500, 0)
    if cactus2.xcor() < -700:
        cactus2.restart(5000, 0)
    if cactus3.xcor() < -700:
        cactus3.restart(5050, 0)
    if cactus4.xcor() < -700:
        cactus4.restart(6500, 0)
    if cactus5.xcor() < -700:
        cactus5.restart(6800, 0)

    # Clouds restart

    if cloud.xcor() < -700:
        cloud.restart(2000, 300)

    if cloud1.xcor() < -700:
        cloud1.restart(1900, 500)
    if cloud2.xcor() < -700:
        cloud2.restart(2000, 400)

    # Add Gravity
    t_rex.new_y += GRAVITY

    # Jump T Rex

    y = t_rex.ycor()
    y += t_rex.new_y
    t_rex.sety(y)
    # Set T Rex to the ground
    if t_rex.ycor() <= 0:
        t_rex.sety(0)
        t_rex.new_y = 0
    # Set T Rex to the ground if it goes too much up
    if t_rex.ycor() >= 500:
        t_rex.sety(0)
        t_rex.new_y = 0

def activate_move():
    stones.move()
    stones2.move()
    stones3.move()
    stones4.move()
    stones5.move()
    stones6.move()
    stones7.move()
    stones8.move()
    stones9.move()

    cactus.move()
    cactus1.move()
    cactus2.move()
    cactus3.move()
    cactus4.move()
    cactus5.move()


    cloud.move()
    cloud1.move()
    cloud2.move()
score = 0
def scoreboard():
    global score
    turtle.pu()
    turtle.hideturtle()
    turtle.goto(500, 500)
    turtle.pd()
    turtle.clear()
    score = int(p / 100)
    turtle.write(f'Score: {score}', align='center', font=('Arial', 18, 'normal'))

game_on = True
p = 0
while game_on:
    screen.update()

    p += 10
    line.forward(p)

    activate_move()
    scoreboard()






    #Detect collision with cactus
    if cactus.distance(t_rex) < 70 or cactus1.distance(t_rex) < 70 or cactus2.distance(t_rex) < 70 or cactus3.distance(t_rex) < 70 or cactus4.distance(t_rex) < 70 or cactus5.distance(t_rex) < 70:
        turtle.goto(0, 0)
        turtle.write("Press 'Space' to play again or 'q' to exit", align='center', font=('Arial', 30, 'normal'))
        turtle.goto(400, 500)
        turtle.write(f'Hi : {score}', align='center', font=('Arial', 18, 'normal'))

        game_on = False
        screen.onkey(play_again, 'space')

        screen.onkeypress(esc, key='q')




    activate_game()











screen.exitonclick()






