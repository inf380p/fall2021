---
layout: post
author: zheinsohn
title: "Zoe's Class Hack and Reflection"
---

Here is the turtle extension I created:
<iframe src="https://trinket.io/embed/python/abb8aaf70d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

It creates a set of 8 triangles in a fan or windmill pattern, and when calling the method you can change the object, heading, color, and size, so if you don't like the windmill pattern, you can change it!


Reflection:
The class modification of changing the color and starting position was fairly simple, because I wanted to focus mostly on the custom method.
I experimented with adding randomizers to the following lines:

```python
    self.setx(-10)
    self.sety(10)
    self.shape("turtle")
    self.color("red")
```
but ultimately settled on specifying the x and y after having some difficulty executing.

However, the biggest difficulty I had was executing the program using following the example syntax to call the method with custom parameters and arguments:

  
`tina.drawSquare` 
or in my case
`sam.DrawTri`

Python didn't seem to want to call the method and continued to return errors.

So I went back to the textbook to look at the syntax there. Although they use slightly different syntax overall, when I modified the call for one of my turtles, sam, to instead use the name of the instantiated object as one of the parameters, like 
  
`DrawTri(sam, 90, "red", 100)`

as written in the textbook, I was able to get the code to run. It was a little frustrating, as it didn't seem to be exactly what I was supposed to do for the assignment, but I was happy enough that I was able to find a workaround that allowed the code to execute and took a break before attempting to rework it.

I tried to use self.begin_fill() and self.end_fill() in the method to fill each triangle with the corresponding color, like so:
```python  
def DrawTri(self, setheading = 0, color = "red", length = 75):
   self.setheading(setheading)
    self.color(color)
    self.pendown()
    self.begin_fill()
    for sides in range(3):
        self.forward(length)
        self.right(120)
    self.end_fill()
    self.hideturtle()
 ```
but found that anything within the larger shape would be filled by the larger shape's color. I quickly realized that the order in which I had asked Python to fill the shapes (small inner triangle first, large outer triangle second) meant that the second "fill" overwrote the first. I swapped the order in which the different sizes of triangles executed, instead filling the largest shape first, followed by the smaller:

`DrawTri(sam, 90, "red", 100)
DrawTri(mike, 90, "blue", 50)
DrawTri(kat, 270, "red", 100)
DrawTri(sky, 270, "blue", 50)`

My original idea was to create a picture of a "windmill" so that adjustments made to the triangles would make different windmills, but I got stuck successfully being able to execute the base of the windmill separately from the triangles. I think a short animation, perhaps utilizing user input to make the windmill "rotate" would be an interesting project.

Overall, I had a lot of fun with this assignment once I successfully was able to call the method. Since I was still a little unsure of exactly how it should look, I used the textbook and previously provided examples as placeholders for a custom method while I made sure my class extension worked. Once the class and the basic method worked, I overhauled the method and experimented with which custom parameters to include. I would like to try to integrate either user input or onscreen clicks and keystrokes. I noticed that with this class hack in particular, I hesitated to make it overly complex out of fear of breaking my code, so I hope to come back to it in the future to modify it without feeling that fear.
