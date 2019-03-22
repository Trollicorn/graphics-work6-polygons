from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians

num = 30
angle = 360/num
for i in range(num):
    screen = new_screen()
    color = [ 255, 255, 255 ]
    edges = []
    transform = new_matrix()
    ident(transform)
    f = open("epic" + str(i) + ".txt",'w')
    f.write("torus\n0 0 0 40 150\n")
#    f.write("rotate\nx 90\n")
    f.write("rotate\ny "+ str(i*angle) + "\n")
    f.write("rotate\nx "+ str(i*angle) + "\n")
    f.write("rotate\nz "+ str(i*angle) + "\n")
    f.write("move\n250 250 0\n")
    f.write("apply\n")
    f.write("save\nuse"+str(i)+".png\n")
    f.close()
    parse("epic"+str(i)+".txt",edges,transform,screen,color)
    remove("epic"+str(i)+".txt")

f = open("gif.sh",'w')
f.write("#!/bin/bash\n\n")
f.write("convert -delay 3x100 -loop 0 ")
for i in range(num):
    f.write("use"+str(i)+".png ")
f.write("art.gif")
