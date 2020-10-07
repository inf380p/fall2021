---
layout: post
author: intjnotinfp
title: "Added intjnotinfp's logical turtle"
---
Here's the code for my logical turtle:
<iframe src="https://trinket.io/embed/python/15e54063fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

On code:
I struggled a little bit with brainstorming /executing this exercise in a timely manner and had to come back later to make improvements to my logical turtle exercise. I was able to satisfy most of the requirements in my code (variables, conditionals, and user input) but got really stumped on how to incorporate operators/operands. When it dawned on me that I could "use math" to just build a shape (I initially didn't want to have to conceptualize and go through the hassle of telling the turtle how far, what angle and what direction to go to make a shape), I looked to the internet for some source code on drawing shapes in turtle. For some reference, at this point I'd only made custom polygons that took too long and looked crappy imo. So, it appeared that a hexagon was quick and easy enough, so after I modified the dimensions, I plugged in the following code and ran the program:

```python
polygon = turtle.Turtle()
my_num_sides = 6
my_side_length = 70
my_angle = 360.0 / my_num_sides
for i in range(my_num_sides):
   polygon.forward(my_side_length)           
   polygon.right(my_angle) 
turtle.done()
```

(** code excerpted from https://www.tutorialspoint.com/turtle-programming-in-python **)

Oops! That had a function in it - I thought I hadn't seen that little word 'for' yet! - and we weren't supposed to use those this go around. I thought about it some more and realized I could just paste the same directions in six times to account for the six sides of the hexagon I wanted to draw and, thank god, that worked and I called it a day.

I'm looking forward to trying the turtlehacks assisgnment next week because I'm hungry to at least attempt something a little more substantial. 

On communication:
I feel quite a bit better about navigating GitHub, especially now that we've had a couple of walk throughs and we worked in pairs to both submit and approve pull requests. Definite confidence boost, but still a little nervous about having to potentially find and resolve a stranger's code problems on GitHub down the line. I really enjoyed having class on Zoom today and I never thought that would come out of my mouth since I fought with everything I had to avoid online classes in the first place. It was cool to work with and talk to my classmates and the screenshare option was 10/10 much better than just following along on the one big screen in class for 3 hours.
