from turtle import*
color("yellow")
begin_fill()
#we want to paint house
width(7)
#step 1: draw a square
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)


pendown()
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing window


penup()
goto(50,140)
pendown()
right(60)
color("white")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
end_fill()
penup()
backward(80)
pendown()
begin_fill()
backward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()





exitonclick()