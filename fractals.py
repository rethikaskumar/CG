#C curve

from turtle import *
color('red')
rule=['r','f','l','l','f','r']
prev=['r','f','l','l','f','r']
ans=[]
for iter in range(4):
    ans = []
    for i in prev:
        if(i=='f'):
            ans+=rule
        else:
            ans.append(i)
    prev = ans
print(ans)
for i in range(0,len(ans)):
    if(ans[i] == 'r'):
        right(45)
    elif(ans[i] == 'f'):
        forward(20)
    elif(ans[i] == 'l'):
        left(45)
done()

#Mandelbrot

import turtle
import math
def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c
# screen size (in pixels)
screenx, screeny = 800, 600
# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)
# discretization step
step = 2
# turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)
screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Computer Graphics")
mTurtle = turtle.Turtle()
mTurtle.penup()
mTurtle.shape("square")
# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny
# plot
for px in range(-int(screenx/2), int(screenx/2), int(step)):
    for py in range(-int(screeny/2), int(screeny/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        m =  mandelbrot(0, x + 1j * y)
        if not math.isnan(m.real):
            color = [abs(math.sin(m.imag)) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(px, py)
    turtle.update()
turtle.mainloop()

#Julia

from PIL import Image
if __name__ == "__main__":
	w, h, zoom = 1920,1080,1
	bitmap = Image.new("RGB", (w, h), "white")
	pix = bitmap.load()
	cX, cY = -0.7, 0.27015
	moveX, moveY = 0.0, 0.0
	maxIter = 255
	for x in range(w):
		for y in range(h):
			zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
			zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
			i = maxIter
			while zx*zx + zy*zy < 4 and i > 1:
				tmp = zx*zx - zy*zy + cX
				zy,zx = 2.0*zx*zy + cY, tmp
				i -= 1
			pix[x,y] = (i << 21) + (i << 10) + i*8
	bitmap.show()

#Dragon

from turtle import *
color('red')
rule=['f','x']
prev=['f','x']
ans=[]
xVals = ['x','+','y','f','+']
yVals = ['-','f','x','-','y']
for iter in range(7):
    ans = []
    for i in prev:
        if(i=='x'):
            ans+=xVals
        elif(i=='y'):
            ans+=yVals
        else:
            ans.append(i)
    prev = ans
for i in range(0,len(ans)):
    if(ans[i] == '+'):
        right(90)
    elif(ans[i] == '-'):
        left(90)
    elif(ans[i] == 'f'):
        forward(20)
done()

#SnowFlake

import turtle

def koch_snowflake(t,length,levels):
    if levels == 0:
        t.forward(length)
        return
    else:
        length = length/3

        koch_snowflake(t, length, levels-1)
        t.left(60)
        koch_snowflake(t, length, levels-1)

        t.right(120)
        koch_snowflake(t, length, levels-1)

        t.left(60)
        koch_snowflake(t, length, levels-1)

t = turtle.Turtle()
t.hideturtle()
t.color('black')

for i in range(3):
    koch_snowflake(t, 200, 4)
    t.right(120)
t.mainloop()

#
