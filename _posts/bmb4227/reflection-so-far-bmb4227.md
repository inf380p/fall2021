---
layout: post
author: bmb4227
title: "Brittany's reflection on the class so far"
---
# Reflection:
I think a lot of lightbulbs went off when I was able to create my custom turtle exerise. I think that was becasue I was able to practice the same skills over and over again and it was a really fun creative project. 
<iframe src="https://trinket.io/embed/python/234ba0a62b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe> 

What's still fuzzy?I think the material that we have covered over the past couple of weeks is definitely still the fuzziest and part of that may be just because it is more complex/or we've covered more content than other weeks. I think what would help with that is 1. practice so if you have a site you would recommend or may some extra optional exercises that might help me and 2. I think if we get a study group going on Thursdays that would be super helpful. I think I end up learning the most when we go over exercises and problems as a class.
An example of what is still fuzzy. When Claire and I were working on our pair project we used:
```python
res = []
for i in romeo:
  #2 search in romeo to see if there are duplicate words
  if i not in res:
    res.append(i)
```
in part of our code. While we were working I was able to recognize and point out that a for I would work but Claire was really the one who understood how to use it and it is still pretty confusing for me personally. 

A useful debugging tool that I really like to use but is probably not the most efficient is to use the # to go through sections. For example, for my clicky hack exercise today I was trying to replicate the GlowTurtle code that you go into in Chapter 2 but for my background color. I kept getting a lot of different errors related to setup and in other parts of my code. So I used comments to comment things out so that I could figure out where the error was occuring but also keep my code so that I could continue to update. For example, like so:
```python
import turtle
from animations import setup
from animations import GlowTurtle
# from animations import background_color_choice 

tina = turtle.Turtle #I erased this at first and only had the glow turtle but it messed things up because new definitions weren't in GlowTurtle
tina = GlowTurtle()
tina.shape("turtle")

myscreen = turtle.Screen()

# This calls your setup function and passes in your screen:
setup(myscreen)
# background_color_choice(myscreen)
```
