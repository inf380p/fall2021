---
author: choim7
title: "Moonjeog's hack assignment and reflection"
---

#trinket embedded link
<iframe src="https://trinket.io/embed/python/3ac5817cc9" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```
#!/bin/python3
from turtle import Screen, Turtle

class Turtlechange(Turtle):
  def __init__(self, name, color, x, y):
    super().__init__(self)
    self.name = name
    self.color(color)
    self.x = x
    self.y = y
    
  def move(self):
    self.penup()
    self.goto(self.x, self.y)
    self.pendown()
    for n in range(5):
      self.forward(15)
      self.left(72)
      self.begin_fill()
      for side in range(5):
        self.forward(15)
        self.right(72)
      self.end_fill()
      if (5 - n) >= 0:
        self.color('red')
      else: 
        break

mia = Turtlechange('mia', 'blue', 50, 50)
cookie = Turtlechange('cookie', 'green', 100, 100)
jack = Turtlechange('jack', 'pink', 150, 150)
mark = Turtlechange('mark', 'grey', 0, 0)
mia.move()
cookie.move()
jack.move()
mark.move()
```

#reflection
At the beginning, one problem I met was str object is not callable. To fix this, I googled online and made some changes when importing turtle class and inherit my 
Turtlechange class from it. Another thing I noticed is when setting up colors, we should use self.color(color) instead of self.color(self.color). The code above
aims to draw a flower figure composed of pentagons with 1 color controlled by parameter and other 4 colors set in red by default. 4 objects were created and each 
of them draw different colors in different positions. In general, I think we should always take care of if we have inherited from super class correctly, otherwise
the code won't run succesfully. 
