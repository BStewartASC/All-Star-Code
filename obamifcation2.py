from Myro import *

darkBlue = makeColor(0,51,76)

red = makeColor(217, 26, 33)

blue = makeColor(112,150,158)

yellow = makeColor(252, 227, 166)

pic = makePicture(pickAFile())
show(pic)

for i in getPixels(pic):
    gray = getGray(i)   
    if gray > 180:
        setColor(i, yellow)
    elif gray > 120:
        setColor(i, blue)
    elif gray > 60:
        setColor(i, red)
    else:
        setColor(i, darkBlue)
       
show(pic)
    
    
 