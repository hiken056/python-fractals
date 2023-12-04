from turtle import *
penup()
pensize(40)
goto(-100,-100)
color('black', 'grey')
pensize(5)
begin_fill()
pendown()


def catHead():
  left(90)
  forward(950)
  right(135)
  forward(400)
  left(45)
  forward(450)
  left(45)
  forward(400)
  right(135)
  forward(950)
  end_fill()


def catFace():
  #eyes
  penup()
  goto(-50, -5)
  pendown()
  forward(100)
  penup()
  goto(50,-5)
  pendown()
  forward(100)
  #nose
  penup()
  goto(-15,-50)
  pendown()
  right(-90)
  forward(150)
  left(-130)
  forward(100)
  right(90)
  forward(100)

catHead()
catFace()

ht()

end_fill()
done()