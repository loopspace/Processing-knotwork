import math
import MathUtils

wd = 20
n = 480/int(math.sqrt(2)*wd)
t = 0

def setup():
    size(480,480)


def draw():
    global t
    background(255)
    translate(240,240)
    scale(1,-1)
    rotate(PI/4)
    noStroke()
    fill(0)
    for x in range(-n,n):
        for y in range(-n,n):
            if abs(x) + abs(y) < n:
                pushMatrix()
                pushStyle()
                translate(x*wd,y*wd)
                stroke(0)
                if (x + y)%2 == 0:
                    rotate(PI/2)
                rotate(MathUtils.step(t,x+y,x+y+1)*TWO_PI)
                line(-wd/2,0,wd/2,0)
                noStroke()
                fill(255)
                ellipse(0,0,5,5)
                stroke(0)
                line(0,-wd/2,0,wd/2)
                popStyle()
                popMatrix()
    t += 1./100
