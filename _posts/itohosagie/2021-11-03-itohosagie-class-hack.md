---
layout: post
author: itohosagie
title: Itohan's Class Hack
---

### Class Hack Reflection: Patterns

After learning how to create turtles last week I wanted to explore the process of creating a pattern since this wasn’t something that I practiced after covering it in the textbook. Maybe I was initially deterred from making patterns because they took so long to run completely, but after discovering the `speed()` method for turtles, I was more willing to give them a shot.

I settled on making circular shapes by using octagons to create a pattern to help solidify the use of `forward()` and directional methods like `left()` and `right()` in creating the shape from a pattern. At first I wasn’t sure what shape I wanted to implement and had some difficulty trying to configure the program to where the size of the shape wasn’t so large and the color called in the method would actually be used when the program ran. As I worked to try and resolve these issues I realized that there were just minor tweaks needed for Python to recognize what I was asking it to do through the program.

For instance, to resolve the problem of the color not adjusting as expected I needed to make sure that `color()` was called within the defined method, in addition to including it as a parameter. Initially my program read as the following:

```
  #defining a method that draws a circular pattern using octagons   
  def pent(self, custom_color = "black"):
    self.pendown()
      #creates the circle
    for i in range(20):
      self.color(“olive”)
      self.forward(10)
      self.right(18)     
      #creates the octagons
      for i in range(8):
        self.color(“maroon”)
        self.forward(80)
        self.right(45)
    self.penup()
```

But after running the program multiple times and cross referencing other programs we’d worked on in class and for homework I remembered that I needed to add the following line of code outside of the `for` loop in order for the color to be adjusted based on whatever argument was used within the method: `self.color(custom_color)` so that the color that was called would actually appear.

Another issue that I ran into while building this program was trying to reduce the size to enable multiple objects to fit in the space. Going back to the section of the book that discussed patterns helped to remind me that the `forward` method called in the portion that creates the octagon determines how large the shape is. Knowing this then I reduced the length from 80 to 45, which helped to leave more space for more than one object. (Code included below)

```
#creates the octagons
      for i in range(8):
        self.color(custom_color)
        self.forward(45)
        self.right(45)
```

After resolving the issue with color I went back and forth between leaving the objects stacked on top of one another with differing pen widths or changing each of their locations individually. Ultimately I chose to set their positions when I called the method for each object by using the `goto()` method to adjust the position of each object.

Here’s a few lines of code where I followed the process outlined above:

```
luca.goto(100,100)
luca.pent("fire pit")
rico.goto(100,-100)
rico.pent("dark goldenrod")
```

Having this chance to work through creating classes and turtles was helpful in furthering my understanding of how these elements work together, but it also was a good refresher for basic aspects of turtles like recalling direction, designating a color, and creating a `for` loop to repeat the turtle. Some things that I would explore further would be to play around with setting the position of the objects randomly as opposed to having to designate their positions manually, as well as introducing another method to create a different turtle and have both turtles running simultaneously. 

The final program is included in the Trinket below.


### Class Hack Trinket

<iframe src="https://trinket.io/embed/python/a696b608d9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
