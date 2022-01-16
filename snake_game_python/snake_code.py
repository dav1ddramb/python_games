import turtle
import random
import time

wn = turtle.Screen()
wn.title('Snake')
wn.bgcolor('black')
wn.setup(width=700, height=700)
wn.tracer(0)


class Snake():
    def __init__(self):
        self.snake = turtle.Turtle()
        self.snake.shape('square')
        self.snake.color('white')
        self.snake.penup()

        #self.snake.goto(0, 0)

    def up(self):
        y = self.snake.ycor()
        return self.snake.sety(y + 2)

    def down(self):
        self.snake.sety(self.snake.ycor() - 2)

    def right(self):
        self.snake.setx(self.snake.xcor() + 2)

    def left(self):
        self.snake.setx(self.snake.xcor() - 2)



# Score
pen = turtle.Turtle()
pen.color('yellow')
pen.penup()
pen.hideturtle()
score = 0
pen.goto(-300, 320)
pen.write(' SCORE: ' + str(score), align='center', font=('Courier', 16, 'normal'))


#s = Snake().snake
#s.goto(0, 0)


# Head
head = turtle.Turtle()
head.shape('square')
head.color('white')
head.speed(0)
head.penup()
head.dir = 'stop'
head.goto(0, 0)
head.pace = 20

food = turtle.Turtle()
food.shape('circle')
food.speed(0)
food.color('yellow')
food.shapesize(stretch_wid=0.75, stretch_len=0.75)
food.penup()
food.goto(random.randint(-350, 350), random.randint(-350, 320))

def add_body():
    body = turtle.Turtle()
    body.shape('square')
    body.color('white')
    body.speed(0)
    body.penup()
    body.pace = 2
    return body


def move():
    if head.dir == 'up':
        head.sety(head.ycor() + head.pace)
    if head.dir == 'down':
        head.sety(head.ycor() - head.pace)
    if head.dir == 'right':
        head.setx(head.xcor() + head.pace)
    if head.dir == 'left':
        head.setx(head.xcor() - head.pace)


def go_up():
    if head.dir != "down":
        head.dir = "up"


def go_down():
    if head.dir != "up":
        head.dir = "down"


def go_right():
    if head.dir != "left":
        head.dir = "right"


def go_left():
    if head.dir != "right":
        head.dir = "left"


wn.listen()

wn.onkey(go_down, 's')
wn.onkey(go_up, 'w')
wn.onkey(go_right, 'd')
wn.onkey(go_left, 'a')


body = [head]
coordinates_x = []
coordinates_y = []

while True:
    wn.update()

    #head.up()
    move()
    if len(body) >= 2:
        for x in range(1, len(body)):
            body[x].setx(coordinates_x[x-1])
            body[x].sety(coordinates_y[x-1])

    if score >= 5:
        head.pace += 0.001
        if score >= 10:
            head.pace += 0.001
            if score >= 15:
                head.pace += 0.001
                if score >= 20:
                    head.pace += 0.001
                    if score >= 25:
                        head.pace += 0.001

    if head.distance(food.xcor(), food.ycor()) <= 15:
        food.clear()
        food.goto(random.randint(-350, 350), random.randint(-350, 350))
        score += 1
        pen.clear()
        pen.write(' SCORE: ' + str(score), align='center', font=('Courier', 16, 'normal'))
        new_body = add_body()
        body.append(new_body)
        new_body.goto(head.xcor(), head.ycor() - 40)

    coordinates_x = []
    for i in range(len(body)):
        coordinates_x.append(body[i].xcor())
    coordinates_y = []
    for i in range(len(body)):
        coordinates_y.append(body[i].ycor())

    time.sleep(0.1)
