import turtle

john = turtle.Turtle()
john.pensize(3)

window = turtle.Screen()
window.bgcolor("lightgreen")

def draw_multicolor_square(t, size):
        for i in ["hotpink","hotpink","hotpink","hotpink"]:
                t.color(i)
                t.forward(size)
                t.left(90)

size = size + 10
for i in range(5):
        draw_multicolor_square(john, size)
        john.forward(10)

window.exitonclick()
