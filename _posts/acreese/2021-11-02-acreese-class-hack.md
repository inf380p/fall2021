---
layout: post
author: acreese
title: "Alex's Class Hack post"
---

# My Extension of the Turtle Class

<iframe src="https://trinket.io/embed/python/d20ad33cf4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

My extenstion of the Turtle class, BoxTurtle, has one new method called random_spiro (that draws random spirographs) and sets the starting turtle state to: a speed of `10` (to draw complicated complex shapes faster), the `"turtle"` shape (of course), the color `"darkmagenta"`, and sends each turtle to the lower left quadrant `(-150,-150)`. And although, it's not part of the class, I set my screen color to `"LemonChiffon"`.

My new method `random_spiro` allows the (box)turtle to draw one or more "random" spirographs based on the parameter entered. 

I call the spirographs random because the number of sides for the inner and outer shapes are both set to random integers between 3 and 7:

```
inner = random.randint(3,7)
outer = random.randint(3,7)
```
...
```
for i in range(inner):   
  self.forward(7)
  self.right(360/inner)
  for i in range(outer):
    self.forward(20)
    self.right(360/outer)
```

They are also *random* because, between every new spirograph, the turtle picks its pen up and travels to a new random location on the screen: 

```
self.penup()
self.goto(random.randint(-150,150), random.randint(-150,150))
self.pendown()
```

And finally, unless the user specifies a single custom color, each spirogrpah will be drawn in a different *random* RGB color. It took me a little while to figure out how to do this, and the resulting code isn't exceptionally elegant, but it works my randomizing integers between 0 and 256 for the three RGB (red, green, blue) values, in the turtle .color() method.
```
self.color(random.randint(0,256),random.randint(0,256),random.randint(0,256))
```

I used my class extention to instantiate four turtles, send them to the four quadrants of the screen, and have them draw different numbers of random spirographs in different colors. The result is a a little messy but interesting to watch unfold. 
```
ant.random_spiro(4, "blue")   #four blue spirographs
bub.random_spiro()            #one random-colored spirograph
cam.random_spiro(6)           #six random-colored spirographs
don.random_spiro(2, "grey")   #two grey spirographs
```
