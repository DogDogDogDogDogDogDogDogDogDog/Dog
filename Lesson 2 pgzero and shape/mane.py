import pgzrun
from random import randint
WIDTH=300
HEIGHT=300
TITLE="square"

def draw():
    WH=5
    HE=5
    R=255
    G=0
    B=randint(120,255)
    for i in range(50):
        recd=Rect((0,0),(WH,HE))
        recd.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(recd,(R,G,B))
        WH=WH+5
        HE=HE+5  
        R=R-1      
        G=G+1
 

def update():
    pass

pgzrun.go()