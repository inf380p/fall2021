---
layout: post
author: intjnotinfp
title: "intjnotinfp's (refactored) functional turtle exercise/ reflection"
---

* intjnotinfp's (refactored) functional turtle exercise/ reflection
** Embedded Code for Purpose of Comparison

Here's my original code - this was from our very first turtle exercise:
<iframe src="https://trinket.io/embed/python/804e40cfa2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

And here's that code with a few additions at the bottom, which served to add (1) plain function and (1) function with parameters to the original:
<iframe src="https://trinket.io/embed/python/dd9c2fe124" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

I'll add just the few lines of code that changed below so that you can look at them as I describe my process.
```#draw a border around the logo
def go_draw_border():
  tina.penup()
  tina.goto(100,150)
  tina.pendown()
  tina.circle(117)

#def add_outro(thanks,congrats)
end = "That's it!"
def print_twice(end):
    print(end)
    print(end)
    
go_draw_border()
print_twice(end)
print_twice(end)
print_twice(end)
```
These were simple functions that either drew a shape or returned text. The first thing I did was play around with coordinates to find the best place to start drawing the border circe. Then I manipulated the size of the circle until it was pretty much centered and encapsulated most of the logo. I ran out of space on the right-hand edge and didn't have the patience to change the coordinates of all my other shapes, so I just rolled with it... Get it? Circle? Anyways. Next, I added text that signaled that the program had finished running so that the user would know not to wait for anything else to happen. I defined a function called Print_twice that would do exactly that. Then, when I called that function three times using end, it showed up on the screen six times.
** Reflection
I really struggled with working through my frustration this week when I got hung up on functions. Although it made sense reading about them, when I tried to put that into practice I was getting one error after another. 
Most of them were syntax errors, which, in theory, should've been easy enough for me to correct by looking at the example format. I realize that the functions I added to this weren't all that exciting (or even useful), but I'm happy to at least have met the requirements and finished it. 
My main takeaway this week was that time management is *important* and I need to be working on these exercises multiple times... Saving it for one sit-down results in disaster when that one session doesn't turn out how you expected. 
I say this tongue-in-cheek and not as whiney as it will sound: that feeling I mentioned the other week about "hacking" something feeling like something akin to a runner's high? Let's just say the highs and the lows balance out :)
On the bright side, I feel a lot more confident about navigating and contributing to GitHub, which I think will be a useful skill down the line. I actually didn't realize this until after this class had started, but a lot of librarians do indeed use GitHub as part of their daily toolset.
I'd like to see what I can really do with Python. I'm not particularly interested in graphics or games, although I do of course see the usefulness in framing basic concepts through those mediums. Even if we don't cover it this semester, I really want to find out what I can make Python do that would automate and simplify basic tasks.

Til next week!

