---
layout: post
author: benderliz
title: "Liz Bender's Class Hack"
---

# Link to my Trinket

<iframe src="https://trinket.io/embed/python/a8cbd4db9b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

In this trinket, I tried my hand at several new turtle-related concepts, such as importing and using the random module, extending the turtle class to create my own subclass, and instantiating several class objects.

At first, I tried creating a program that would make turtles "fight" in a ring (big circle), but I read online that it is impossible for turtles to move at the same time. I am not sure if this is 100% accurate, but I thought I had better leave this quest to the experienced programmers for now. Maybe my turtle game will involve some reptilian MMA.

I then decided to create a program that would have turtles draw concentric circles, with each turtle being assigned a random color. To do this, I first imported the turtle module, as well as the random module so that my turtle objects could later be assigned random colors.
Then, I created a gray screen and defined the list of "random" colors from which the turtles can draw. Next, I began the epigrammatic portion of this assignment: creating a subclass of turtle, aptly named, 'ConcentricTurtle'. I set the turtle shape, color, and speed.

When creating the subclass, I needed to define the function that would actually draw the circles. This is where I utilized our good friend Google to make sure I got the concentric circles right. 
I got stuck here, because I did not realize I needed to create a color method for the color to be randomly assigned (at the end of the program). I am definitely still fuzzy on methods.

  ```
  # draw concentric circles with start argument so circles don't have to overlap'
  # create color method
  def concentric(self, color, start):
    self.color(color)
  ```

Conceptually, the idea of "self" being needed to instantiate is still a little confusing to me. For instance, in the following lines, I don't know why the self argument does not need to be included. Or, perhaps, I don't know why it is necessary at all. I think in class we talked abut how it is not much more than a formality, though.

```
# use the concentric method to draw 4 circles with a random color from the above list
tito.concentric(random.choice(color_list), 1)
```

Goodbye for now,

Liz
