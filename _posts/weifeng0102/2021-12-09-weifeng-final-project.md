---
layout: post
author: weifeng0102
title: "Weifeng's final project!"
---

# Trinket
<iframe src="https://trinket.io/embed/python/3ef9d88848" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Recorded presentation
https://utexas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7b94e6af-95aa-43df-8619-adf900bfb248

# Reflection
I want to make a small treasure hunting game. Players can use the keyboard to operate the turtle to move up, down, left, and right. There are some treasures (yellow triangles) and stones (black squares) in the field. When the players encounter treasure, they can eat it.If you reach the stone and hit it, you will lose, and the game will win after you eat all the treasures.

In the process, I encountered some obstacles, but solved them through my own efforts. For example, at the beginning, I wanted to split all the defined function codes into different files for easy management. The intersection is placed in one file, and the keyboard control is placed in another file, but there is still no way to complete the intersection operation. I later merged the two codes into one file, and added a check_intersect code to each keyboard operation to achieve it successfully.

But there are also some unresolved problems. For example, I designed the display of the result of game failure, but I have not been able to make the functions of success and failure take effect at the same time. This is an important problem that I will try to solve next. Later I found out that this was because of an error in my intersecting coordinates, and I tried to solve it later.

Another one problem is that it bothers me to wait for drawing pictures every time I run the program. Later, after observing other people’s codes, I found that they are very fast in turtle drawing, so I tried to find some drawing codes on the Internet and found out. It turned out that the turtle's movement speed was not set. After setting the speed to 0, the problem was finally solved. I can draw the basic pattern immediately later, which greatly improves my efficiency.

I encountered a problem when trying to write the code of the intersection function. Although the code can run successfully and the corresponding result can be successfully triggered after the intersection is triggered, there is a problem with the trigger position, and there will be no response when the turtle and the stone intersect. But it will be triggered when the turtle reaches a certain distance from the stone, but I don't know what the reason is. It may be that the intersection target is written incorrectly, or the intersection coordinate design is wrong. In order to find out the reason, I came up with a method, which is to draw 3 random stones, and then define a color-changing function. When the turtle touches the stone, the corresponding stone will change color, so I know through the test which position can trigger the intersection with which stone.

After many tests, I found that when I set the x and y coordinates of the stone to be the same, the turtle can trigger the intersection function at the correct position, and the intersection reaction of the stone with coordinates (x, y) will occur Coordinates (x, x), so I checked my intersecting function code, and finally found the problem.
```python
  def intersect(self, object):
    
    xbounds = (self.xcor()-self.radius, self.xcor()+self.radius)
    ybounds = (self.ycor()-self.radius, self.ycor()+self.radius)
    x, y = object.pos()
    check_x = x > min(xbounds) and x < max(xbounds)
    check_y = y > min(xbounds) and y < max(xbounds)
    if (check_x and check_y):
      return True
    else:
      return False
```
The ybounds in the check_y part is wrongly written as xbounds. This mistake was very stupid, but I spent a lot of time correcting him. This incident made me realize how important it is to be rigorous and careful. Although the error is small, I have learned a lot in the process of correcting the error. I am very excited to find the cause of the code error through the analysis step by step. This process makes me feel very excited, and finally solves the problem on my own. It is also very fulfilling. 

Solved the intersecting problem. I quickly completed the code for the two states of game success and game failure, but in order to make the game performance more vivid, I hope that when turtle comes into contact with treasure, there will be an effect of eating it. So when they intersect, the treasure will disappear. My first idea is to make the treasure the same color as the background. But in the previous code, the treasure I set is a painted star:
```python
class star(turtle.Turtle):
  def __init__(self,x,y,size=20):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.goto(x,y)
    self.pendown()
    self.begin_fill()
    self.color('yellow')
    for i in range(5):
      self.forward(size)
      self.right(144)
    self.end_fill()
    self.penup()
    self.radius = 20
```
This caused a problem. When I wanted to make it disappear, there was no way to directly use self.color() to change its color, so in order to make it easier to implement, I changed the drawn star directly to shape:
```python
class treasure(turtle.Turtle):
  def __init__(self,x=0,y=0):
    turtle.Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.goto(x,y)
    self.pendown()
    self.color('yellow')
    self.shape('triangle')
    self.radius = 20
```
So I can directly change the color of treasure with self.color():
```python
  def change(self):
    self.color(‘green’)
    return
```
After trying, there is still a small problem, that is, when I manipulate the turtle to touch the treasure, it will be partially blocked, so I directly changed the code for changing the color to hide the treasure:
```python
  def change(self):
    self.hideturtle()
    return
```
This successfully achieved the effect of eating treasure.

The implementation of a single level is completed like this. I thought that multiple levels only need to copy the same code a few times to complete, but in fact it is not as simple as I thought. Because of the single level, my design method is to define the drawing method of stone and treasure and then draw their positions one by one:
```python
a = stone(-100,-100)
b = stone(100,100)
c = stone(0,0)
d = stone(-50,-50)
e = stone(30,60) 
f = stone(60,30) 
g = stone(-120,-30) 

t1 = treasure(0,100)
t2 = treasure(0,-100)

stones = [a,b,c,d,e,f,g]
treasures = [t1,t2]
```
But the problem with this is that I need to draw the position of each stone and treasure one by one for each level. This is not only inefficient, but also inconvenient to manage when modifying the game settings, and I don’t know how to put each one. The levels are connected in series. In order to solve this problem, I watched the professor’s instructional video on OREILLY, changed the definition code of stone and treasure to the following, and added the functions of makestone and maketreasure, so that the number corresponding to the level can be quickly generated in the corresponding level The stone and treasure.
```python
class stone(turtle.Turtle):
  def __init__(self,x=0,y=0):
    turtle.Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.setpos(randint(-180,180),randint(-180,180))
    self.pendown()
    self.color('black')
    self.shape('square')
    self.radius = 20
    self.hit = False

def makestones(n):
  screen.tracer(0)
  stones = []
  for i in range(n):
    newstone = stone()
    stones.append(newstone)
  screen.tracer(1)
  return stones
```
In addition, I also learned from the code on the level setting inside, store the information of each level in the dictionary, and then use the variable n to set various contents of the corresponding level. Some changes have been made to my scoring method. My score calculation is not based on the number of treasures the player has obtained, because the player must obtain all the treasures to pass the level, so I hope that the faster the player can pass the level, the higher the score they can get. First, set an initial time t0 = clock(). After all the treasures in the level are eaten, the timing is over and the score is calculated:
```python
  hittreasure = []
  for treasure in treasures:
    hittreasure.append(treasure.hit)
  
  if False not in hittreasure:
    for treasure in treasures:
      treasure.hideturtle()
    
    time = int(clock()-t0)
    score = int(1000/time)
```
Finally, add the scores of all relevant cards to get the final result. My initial plan was to display the time and score at the end of each level, but there is not enough time to complete it, and I will continue to improve it in the future.

In the process of completing this project, I felt a little bit from the beginning and finally completed it. I felt very fulfilled. In this process, I also encountered many obstacles. For example, when the program can run successfully but it is different from the ideal effect, it crashes because I don't know what went wrong. So you need to explore and correct mistakes step by step by yourself. This process is painful and fun. The interesting part is that it is very exciting to realize the code a little bit in the process of learning.

