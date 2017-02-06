import turtle

def draw_multicolor_square(t, sz):
        for i in ["hotpink","hotpink","hotpink","hotpink"]:
                t.color(i)
                t.forward(sz)
                t.left(90)
                

window = turtle.Screen()
window.bgcolor("lightgreen")

john = turtle.Turtle()
john.pensize(3)

size = 20
for i in range(5):
        draw_multicolor_square(john, size)
        john.forward(10)
        john.penup() 
        john.forward(50)
        john.pendown()
        

window.exitonclick()
