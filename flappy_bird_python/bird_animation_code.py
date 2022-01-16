import turtle


wn = turtle.Screen()
wn.bgcolor("Black")
t = turtle.Turtle()
t.speed(0)
t.pensize(4)

def birdie():
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.color("yellow")
    t.end_fill()
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.color("red")
    t.end_fill()
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.color("yellow")
    t.forward(20)
    t.right(90)
    t.color("yellow")
    t.end_fill()
    t.color("black")
    t.forward(20)

birdie()


#def square():
 #   t.begin_fill()
  #  birdie()
   # t.color("yellow")
    #t.end_fill()
    #t.color("black")
    #t.forward(20)


#square()



#def bird_anim():
    #for x in range(3):
     #   t.forward(20)
      #  t.color("Yellow")
       # t.end_fill()
        #t.color("Black")


#bird_anim()