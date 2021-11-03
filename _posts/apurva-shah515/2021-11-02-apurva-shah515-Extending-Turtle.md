---
layout: post
author: apurva-shah515
title: "Apurva's Extended Turtle Class and Reflections"
---
# Reflection

This week I have been playing with extending the base turtle class, and incorporate some randomness within my program through the random module. The first challenge this week was to extend the base Turtle class by moving the turtle to a new position, and by giving it a new color. Giving the turtle a new color was relatively simple, and I make use of the `self.color("gold")` method to do so in my program. 

The starting point for creating a new class was the same as we observed in last week's class, by taking the existing Turtle and initiating the new class with the same methods as the existing Turtle class. 

```python
class StarTurtle(turtle.Turtle):
  # Overriding the default settings
  def __init__(self):
    turtle.Turtle.__init__(self)
```

I decided to incorporate a method from the random module for changing the starting position of the Turtle. This would ensure that every new object instantiated has a random starting position. Making use of the random module to create variance between different objects and the overall space that the Turtles are in added a new layer of depth to what I could use with Turtles, and how I might make use of this in our final project should I choose to make a Turtle game. 

```python
# Move the new turtle to a random position within a space
x = random.randint(-150, 150)
y = random.randint(-150, 150)
self.setposition(x, y)
```    

Thus I had created a new class, called StarTurtle. The next step was to add a new method to this new class I had created. To do this, I made use of the draw_star method I had defined from the previous week's turtle trinkets. I added some modifications to suit it being added to the new Turtle class, such as the `self.pendown()`, and `self.penup()` commands at the beginning and end of the new method. I also added color as a parameter for this method such that I could change it when calling on the Turtle to perform the method. 

```python
# Adding a method for drawing a star which takes color as an input
  def draw_star(self, color = 'gold'):
    self.pendown()
    self.color(color)
    for x in range(50):
          self.forward(40)
          if x % 2 == 0:
              self.left(175)
          else:
              self.left(200)
    self.penup()
```

The last portion of added 'spice' to me new Turtle program led me to explore how I can randomly assign a color to the new method. Given that Turtle has a list of colors that it can take, fiddling with the program led me to create a list of several colors that I had chosen from the color palette within Trinket. 

```python
# A list of colors that a turtle can take  
color_list = ['crimson', 'red', 'blue', 'green', 'wheat', 'royal blue', 'silver', 'dark orchid', 'gold']
```
From this point I then made use of a method from the random module, `random.choice()`, to select one color from the above list for the draw_star method. This allowed me to add a new layer of randomness to the overall program and also explore how I can use randomness from within a list of items, as opposed to just integers. 

```python
# Using the draw_star method to draw 4 stars with a random color from the above list
bob.draw_star(random.choice(color_list))
milly.draw_star(random.choice(color_list))
lisa.draw_star(random.choice(color_list))
terry.draw_star(random.choice(color_list))
```
Overall this was a very interesting exercise, and playing with the random module to create variance and visual depth using the Turtle module was very intriguing. I still feel that using Turtle is very intuitive and so this exercise was not particularly taxing, however playing around with the randomness helped with pushing the boundary of my understanding and led me to think of some interesting opportunities for further extension. 

# The full program in Trinket

<iframe src="https://trinket.io/python/84c65ab269" width="100%" height="600" frameborder="0" marginwidth="0" allowfullscreen></iframe>
