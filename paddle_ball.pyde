from time import sleep
from random import randint


x = (300)
y = (300)

directionY = randint(-10,10)
directionX = randint(-10,10)
speed = 1

def setup():
    size(600,600)

def draw():
    background(22, 220, 100)
    global x
    global y
    global speed
    global directionX
    global directionY
    x = x + speed*directionX
    y = y + speed*directionY
    if x <= 0 or x >= 600:
        directionX = directionX * -1
    elif y <= 0 or y >= 600:
        directionY = directionY * -1
    noStroke()
    fill(255,0,0)
    ellipse(x,y,20,20)
    fill(30, 26, 199)        
    rect(mouseX, 550, 140, 15)
    if 



    
    
    
    