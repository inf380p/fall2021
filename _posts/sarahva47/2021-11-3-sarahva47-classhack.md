---
layout: post
author: sarahva47
title: "Sarah Varenhorst's class hack exercise and reflection"
---
This is my Trinket post:
<iframe src="https://trinket.io/embed/python/a431adc3f6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

For the Class Hack exercise, I needed to extend the Turtle class, instantiate four objects, and add a new method to the turtle class. To do this, I started by setting up the turtle and overriding some defaults. I changed the turtle's speed, which goes on a scale from 1 to 10, to 6 to make it draw faster. I also changed the color to blue and made the cursor a circle. I chose a circle to stand in contrast with the angular polygons I'm making. I chose to call this class CircleTurtle because the shape of the turtle is a circle. Here, I played around with the settings after finishing the rest of the turtle so that I could see how changes to the class affect the rest of the program. I messed with the speed a few times to get slower or faster feedback. At first, I messed up with conflating "goto" and "setheading." Thankfully, an error message appeared that "setheading" can only take on one parameter, which clued me in that it would not take a coordinate and I checked my notes to remember that "goto" was the correct option to place the turtle in a different starting position. I then used "setheading" to angle the polygon. I also, for changing the turtle shape, did not know what shapes the turtle could take. The textbook, at least so far, has not covered this and it wasn't brought up in class. Therefore, I got the amusing experience of tiredly Googling "what shapes do turtles know" and getting some interesting articles on turtle psychology instead! After adding the word "Python," I did eventually learn that turtles can be circles, turtle-shaped, triangles, squares, arrows, or small "classic" arrows. I'm now left curious about the choices for these shapes since 50% of them are triangles of some form. I would love to see a heart or star shape used. 
```
class CircleTurtle(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    
    self.speed(6) #speed can go 1-10
    self.penup()
    self.shape("circle")
    self.color("blue")
    self.setheading(45)
    self.goto(-150,25) #starting position is in the top left quadrant
    self.pendown()
 ```   
 For the next part of the assignment, I honestly didn't remember what it meant to "instantiate" objects, so I ended up Googling the definition. After clearning that up, I instantiated four turtle objects that are all references to Taylor Swift's Folklore album for the names.
```
betty = CircleTurtle()
james = CircleTurtle()
inez = CircleTurtle()
augustine = CircleTurtle()
```
I then chose to make a method to draw a polygon next in my program. The method allows the user to change the turtle's starting position so that when it runs, you can see the blue circle fly across the screen to another point. The user can also change the colors so that each time the method is used, it's obvious which one is which. The turtle makes a ten-sided polygon in a larger pen size (5). At the end of the method, the turtle's cursor is hidden so that you just see the polygons.
```
def draw_polygon(x, y, color, self):
  self.penup()
  self.goto(x,y)
  self.pensize(5)
  self.color(color)
  self.pendown()
  for side in range(10):
    self.forward(25)
    self.left(36)
  self.hideturtle()
 ```
I finished by using draw_polygon four times, one for each turtle object, and gave parameters around the screen and with different colors so you can see the polygons being formed around the screen.
```
draw_polygon(150, 50, "red", betty)
draw_polygon(-150, -50, "pink", inez)
draw_polygon(-150, 50, "violet", james)
draw_polygon(150, -50, "purple", augustine)
```
At this point, my program does four things. I'm still a little fuzzy on if I followed the directions for the assignment correctly, but I'm fairly confident it follows the directions at least well enough to go ahead and submit it. I think I need to brush up on Python vocabulary a little more like "instantiate." 
