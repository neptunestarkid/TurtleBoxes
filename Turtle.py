# all the the Turtle Module
import turtle

def boxes():
    # set the shape
    turtle.shape("turtle")

    # set turtle.Turtle to variable my_turtle
    my_turtle = turtle
    turtle.pensize(6)
    turtle.color("green", "blue")
    turtle.turtlesize(3,3,6)

    # begin color fill
    ## to be called just before drawing a shape to be filled
    turtle.begin_fill()

    # make the big box
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)

    # end color fill
    ## fill the shape drawn after the last call to begin_fill()
    turtle.end_fill()


    # move to make little boxes
    my_turtle.left(90)
    my_turtle.forward(100)

    # change the fill color
    turtle.color("green", "yellow")

    # begin color fill
    turtle.begin_fill()

    # start to make little left box
    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()



    # start to make little top box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "red")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # start to make little left box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "green")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # start to make little bottom box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "purple")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # hide the turtle
    my_turtle.hideturtle()

    # pull pen up
    turtle.penup()
    turtle.goto(-200, 0)

    ######### start new boxes ##########

    # set the shape
    my_turtle.showturtle()
    turtle.pendown()
    turtle.shape("turtle")

    # set turtle.Turtle to variable my_turtle
    my_turtle = turtle
    turtle.pensize(6)
    turtle.color("green", "blue")
    turtle.turtlesize(3,3,6)

    # begin color fill
    ## to be called just before drawing a shape to be filled
    turtle.begin_fill()

    # make the big box
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)

    # end color fill
    ## fill the shape drawn after the last call to begin_fill()
    turtle.end_fill()


    # move to make little boxes
    my_turtle.left(90)
    my_turtle.forward(100)

    # change the fill color
    turtle.color("green", "yellow")

    # begin color fill
    turtle.begin_fill()

    # start to make little left box
    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()



    # start to make little top box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "red")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # start to make little left box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "green")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # start to make little bottom box
    my_turtle.right(90)
    my_turtle.forward(25)

    # change the fill color
    turtle.color("green", "purple")

    # begin color fill
    turtle.begin_fill()

    my_turtle.left(90)
    my_turtle.forward(25)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)

    # end color fill
    turtle.end_fill()

    # hide the turtle
    my_turtle.hideturtle()
    
    return
boxes()






