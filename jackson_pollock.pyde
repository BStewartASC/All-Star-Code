from random import *

def setup():
    size (500, 500)
    
def draw():
    fill(randint(0,255),randint(0,255),randint(0,255))
    noStroke()
    ellipse(mouseX, mouseY, 55, 55)
    for i in range(20):
        x = randint(20,35)
        ellipse(mouseX + 40, mouseY + 50, x, x)
        fill(randint(0,255),randint(0,255),randint(0,255))
        
    