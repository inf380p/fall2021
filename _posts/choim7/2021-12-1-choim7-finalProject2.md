---
layout: post
author: choim7
title: "Moonjeog's final project plan"
---

#I would like to make a Turtle game for my final project. I want to make a superman pong game in which the interface includes 2 paddles and 1 ball and the background image is a superman logo. I think I should look through more Turtle methods for completing my final project. 
I will go through the Turtle instructions on Python website at first and go to the Pygames to see what interesting elements I can add to my project:)

#The following is the embeded link to trinket
<iframe src="https://trinket.io/embed/python3/5d0c9a8e05" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
# import turtle library 
import turtle

# setup screen 
sc = turtle.Screen()
sc.title("Ping-Pong Game")
sc.setup(width=1000, height=700)
#I will use turtle to draw a superman background
 
# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)![pong](https://user-images.githubusercontent.com/89755399/142249999-4a2f9c75-1a33-4d7c-b964-895883e8051d.jpg)

right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
left_player = 0
right_player = 0
 
 
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))
 
 
# Functions to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
 
#other methods for user&game interactions will be added on later 
```


#The code above is referred to a code from the online resource. I will add a superman background later and makes some changes of this code. I think to make a pong game might not be that hard since online resources give lots of hint on how to do it. I may want to combine mario game with the pong game maybe. 

![pong](https://user-images.githubusercontent.com/89755399/142250060-9a81e450-e2b4-4dcc-b14a-508c8828b8a8.jpg)
