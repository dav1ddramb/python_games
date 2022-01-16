import turtle
import random

wn = turtle.Screen()
wn.title('Flappy Bird Custom')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Bird

# try class Bird

bird = turtle.Turtle()
bird.shape('square')
bird.color('yellow')
bird.penup()
bird.goto(-250, 0)

bird.dy = -2.5


# Score
attempts = 0
score = 0
score_list = [0]
#best = max(score_list)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(-320, 220)
pen.write(' Score:' + str(score) + '\n' + ' Attempts:' + str(attempts) + '\n' + ' Best:' + str(max(score_list)),
          align='center', font=('Courier', 16, 'normal'))

tut = turtle.Turtle()
tut.speed(0)
tut.color('white')
tut.penup()
tut.hideturtle()
tut.goto(-320, 30)
tick = 0


# Hurdles
class Hurdles():
    def __init__(self):
        self.hurdle_obj = turtle.Turtle()
        self.shape = self.hurdle_obj.shape('square')
        self.color = self.hurdle_obj.color('green')
        self.penup = self.hurdle_obj.penup()
        self.shapesize = self.hurdle_obj.shapesize(stretch_len=3, stretch_wid=17)
        self.hurdle_obj.dx = -1

    #def speed(self):


hurdle1_down = Hurdles().hurdle_obj
hurdle1_up = Hurdles().hurdle_obj
hurdle1_down.goto(50, random.choice([-270, -200, -150, -90]))
hurdle1_up.goto(50, hurdle1_down.ycor() + 450)

hurdle2_down = Hurdles().hurdle_obj
hurdle2_up = Hurdles().hurdle_obj
hurdle2_down.goto(240, random.choice([-270, -200, -150, -90]))
hurdle2_up.goto(240, hurdle2_down.ycor() + 450)

hurdle3_down = Hurdles().hurdle_obj
hurdle3_up = Hurdles().hurdle_obj
hurdle3_down.goto(430, random.choice([-270, -200, -150, -90]))
hurdle3_up.goto(430, hurdle3_down.ycor() + 450)


#for i in range(0, 400, 150):
 #   hurdle_down = Hurdles().hurdle_obj
  #  hurdle_down.goto(i, random.choice([-180, -150, -120, -90]))
   # hurdle_up = Hurdles().hurdle_obj
    #hurdle_up.goto(i, hurdle_down.ycor() + 450)

# Function
def jump():
    y = bird.ycor()
    y += 50
    bird.sety(y)
    global tick
    tick = 1



#def hurdle_gen(l, resp):


def hurdle_gen(x_cor):
    hurdle_down = Hurdles().hurdle_obj
    hurdle_down.goto(x_cor, random.choice([-270, -200, -150, -90]))
    hurdle_up = Hurdles().hurdle_obj
    hurdle_up.goto(x_cor, hurdle_down.ycor() + 450)

    #hurdle_up.dx = -1
    #hurdle_down.dx = -1

# Keyboard binding
wn.listen()
wn.onkeypress(jump, 'w')

while True:
    wn.update()

    tut.clear()

    bird.sety(bird.ycor() + bird.dy)

    hurdle1_down.setx(hurdle1_down.xcor() - 2)
    hurdle1_up.setx(hurdle1_down.xcor() - 2)

    hurdle2_down.setx(hurdle2_down.xcor() - 2)
    hurdle2_up.setx(hurdle2_down.xcor() - 2)

    hurdle3_down.setx(hurdle3_down.xcor() - 2)
    hurdle3_up.setx(hurdle3_down.xcor() - 2)

    if tick == 0:
        tut.write(' PRESS w TO JUMP', align='center', font=('Courier', 16, 'normal'))
        tut.clear()


    if - 290 <= hurdle1_up.xcor() <= -220:
        # Crash
        if hurdle1_down.ycor() + 180 >= bird.ycor() or hurdle1_up.ycor() - 180 <= bird.ycor():
            hurdle1_down.goto(50, random.choice([-270, -200, -150, -90]))
            hurdle1_up.goto(50, hurdle1_down.ycor() + 450)
            hurdle2_down.goto(240, random.choice([-270, -200, -150, -90]))
            hurdle2_up.goto(240, hurdle2_down.ycor() + 450)
            hurdle3_down.goto(430, random.choice([-270, -200, -150, -90]))
            hurdle3_up.goto(430, hurdle3_down.ycor() + 450)
            bird.goto(-250, 0)
            attempts += 1
            score_list.append(score)
            score = 0
            pen.clear()
            pen.write(' Score:' + str(score) + '\n' + ' Attempts:' + str(attempts) + '\n' + ' Best:' +
                      str(max(score_list)), align='center', font=('Courier', 16, 'normal'))
        else:
            if -290 <= hurdle1_down.xcor() <= -288:
                #hurdle_down.goto(50, random.choice([-180, -150, -120, -90]))
                #hurdle_up.goto(50, hurdle_down.ycor() + 450)
                score += 1
                pen.clear()
                pen.write(' Score:' + str(score) + '\n' + ' Attempts:' + str(attempts) + '\n' + ' Best:' +
                          str(max(score_list)), align='center', font=('Courier', 16, 'normal'))

                #hurdle1_down, hurdle2_down = hurdle2_down, hurdle1_down
                #hurdle1_up, hurdle2_up = hurdle2_up, hurdle1_up
                #hurdle2_down.goto(100, random.choice([-180, -150, -120, -90]))
                #hurdle2_up.goto(100, hurdle2_down.ycor() + 450)

                hurdle3_up, hurdle2_up, hurdle1_up = hurdle1_up, hurdle3_up, hurdle2_up
                hurdle3_down, hurdle2_down, hurdle1_down = hurdle1_down, hurdle3_down, hurdle2_down
                hurdle3_down.goto(290, random.choice([-270, -200, -150, -90]))
                hurdle3_up.goto(290, hurdle3_down.ycor() + 450)

    #hurdle_gen(50)

    # Out of Bounds
    if bird.ycor() < -290 or bird.ycor() > 290:
        hurdle1_down.goto(50, random.choice([-270, -200, -150, -90]))
        hurdle1_up.goto(50, hurdle1_down.ycor() + 450)
        hurdle2_down.goto(240, random.choice([-270, -200, -150, -90]))
        hurdle2_up.goto(240, hurdle2_down.ycor() + 450)
        hurdle3_down.goto(430, random.choice([-270, -200, -150, -90]))
        hurdle3_up.goto(430, hurdle3_down.ycor() + 450)
        bird.goto(-250, 0)
        attempts += 1
        score_list.append(score)
        score = 0
        pen.clear()
        pen.write(' Score:' + str(score) + '\n' + ' Attempts:' + str(attempts) + '\n' + ' Best:' + str(max(score_list)),
                  align='center', font=('Courier', 16, 'normal'))