import turtle
import random

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Bounce Ball")
wn.tracer(0)

balls = []

for _ in range(30):
    balls.append(turtle.Turtle())


# Randomizing ball color

colors = ["green", "blue", "purple", "pink", "white", "aqua", "red", "orange"]
shapes = ["circle", "square", "triangle"]

# Creating ball
for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(1)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

# Creating gravity for the ball
gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # Check for a collision
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1

        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1

        # Check for a bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1


wn.mainloop()

