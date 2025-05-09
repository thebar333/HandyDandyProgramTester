from turtle import *
import random
n = 400
speed(10000)
colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from
for i in range(400):
    forward(n)
    colour = random.choice(colors)
    color(colour)
    circle(8, extent=150)
    n = n-1
