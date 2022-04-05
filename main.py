import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def drawSineCurve(dart):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  for i in range(-360,360):
    yvar = math.sin(math.radians(i))
    dart.goto(i,yvar)
def setupWindow(window):
  window.setworldcoordinates(-360, -1, 360, 1)
def setupAxis(dart):
  for i in range(4):
    dart.up()
    dart.goto(0,0)
    dart.down()
    dart.forward(360)
    dart.left(90)
def drawCosineCurve(dart):
  dart.up()
  dart.goto(-360, 1)
  dart.down()
  for i in range(-360, 360):
    yvar = math.cos(math.radians(i))
    dart.goto(i,yvar)
def drawTangentCurve(dart):
  dart.up()
  dart.goto(-360,0)
  dart.down()
  for i in range (-360, 360):
    yvar = math.tan(math.radians(i))
    dart.goto(i,yvar)
def drawCotangentCurve(window,dart):
  window.setworldcoordinates(-1,-1,1,1)
  dart.up()
  dart.goto(360, 0)
  dart.down()
  dart.color("red");
  for i in range(0,360):
    dart.goto(math.cos(math.radians(i)), math.sin(math.radians(i)))
    
  
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    curve = input("Which curve do you want to draw? (Choose one: sin, cos, tan, circle)")
    if (curve == "sin"):
      drawSineCurve(dart)
    if (curve == "cos"):
      drawCosineCurve(dart)
    if (curve == "tan"):
      drawTangentCurve(dart)
    if (curve == "circle"):
      drawCotangentCurve(wn,dart)
    wn.exitonclick()
main()
