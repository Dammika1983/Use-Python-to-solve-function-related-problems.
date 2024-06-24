#
# Create a function that draws a square, pass in as an argument, the size of the square
# Writen by: Dammika Pathirana
# Date: June 23, 2023
#
#Import turtle
import turtle

#Desighn a turtle object
t = turtle.Turtle()

#Decalre the function
def draw_square(width,height):
    for i in range(4):
        t.fd(width)
        t.rt(90)
        t.fd(height)
        t.rt(90)

#call the function
draw_square(7,7)






