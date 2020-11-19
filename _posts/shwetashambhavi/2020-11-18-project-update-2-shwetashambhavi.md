---
layout: post
author: shwetashambhavi
title: "Shweta Project Update & Report 2"
---

**Embedded Trinket**
<iframe src="https://trinket.io/embed/pygame/2d3ea42077" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Code Snippet**
```python

class clouds(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.penup()
    self.shape('circle')
    self.pencolor('white')
    self.fillcolor("white")
 
  
    self.onclick(lambda x, y:self.handle_click(x,y))
  
  def draw(self,p):
    self.penup()
    self.setpos(p[0],p[1])
    self.pendown()
    self.begin_fill()
    .......

  def handle_click(self,x,y):
    self.penup()
    self.setpos(x,y+30)
    self.pendown()
    self.fillcolor("yellow")
    ......
```   
**Reflection**
I had a rough start using the Python3 trinket and got sidetracked with the Pygame module. I was facing problem with the closing of the window after code execution and couldn't find an easy fix on my own. With some help in class, I realised that I didn't need the Pygame module and the turtle's done() method can do this job. So there' delay in achieving my initial milestones but, I think I can get there with some work. 

Till now, I've made a basic design for the 1st canvas with the cloud class. Next, I'll be completing both the canvases with a toggle option and house on the screen. After my canvas is complete, I would like to add balloon features into it. My goal for next week will be to at least have all of this ready with the motion of house enabled.
