---
layout: post
author: AU-turtledragon
title: "Aaron's two trinket post and reflection."
---

# My Runestone Trinket:

<iframe src="https://trinket.io/embed/python/fc092489c1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# My Freeform Trinket:

<iframe src="https://trinket.io/embed/python/5fc3aa7734" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection:

For my freeform turtle assignment, I was a little short on ideas and therefore wrote something fairly simple.  My script defines a function drawshape, which takes a turtle, a shape name, a color, a pen size, and an overall shape size to draw shapes according to those specifications.  Due to time constraints, my code is fairly limited in that it can only draw three shapes (square, triangle, and circle) in two size options (big and small), and anything outside of those parameters triggers an error animation and an apology statement.  

Overall, I found this week’s lesson and exercise to be fairly straightforward and the logic behind it all fairly easy to understand.  Since our textbook teaches more by example than explanation, there were certain areas I found difficult to intuit on my own at first but eventually managed to deduce what was going on.  Most of this had to do with the placement and directional orientation after certain actions had taken place.  For instance, when the goto method was introduced within an exercise, I couldn’t figure out how such a move affected affected the turtle’s orientation after being moved.  In my mind, the turtle was essentially teleporting to the new location and upon landing would assume its default eastward orientation.  Eventually, I came to realize it’s actually more of an actual directional command, after which the turtle remains in the same orientation it was in before it moved.  Likewise, for the same reason, I wasn’t sure why I needed to penup before executing a goto.  But, a simple test run made that pretty clear. 

Other than that, the only areas that seem to be tripping me up are certain syntax details, and most often that involves capitalization.  It’s a simple thing and I’m getting a feel for it through repetition, but remembering that capitalization of an object class (at least I think that’s what we’re dealing with there) is critical.  Likewise, I don’t feel I have a firm grasp on what’s being articulated in statements like “from turtle import *”, which makes them hard to remember.  I tend to make my way through this code by thinking through the thing I’m actually asking, rather than rote memorization.  But, when I don’t quite understand the syntax, memorization is all I can do. And that’s coming through repetition. But, it will just as easily go if/when I’m not writing Python code every single week, which kind of bothers me.  

Looking at my code more specifically, I’m not sure I would write it the same if I was doing this assignment over.  I had a lot on my plate this week, and by the time I got this working right, I had to just be satisfied that it did what it set out to do, albeit in a limited fashion.  But, I realize it’s not very efficient.  Looking back at how I’ve constructed the conditionals to determine which shapes to draw etc, I realize that these conditional statements aren’t really simplifying anything that couldn’t just as easily be done via a handful of separate functions for each shape.  At some point, when I have more time, I might go back over it to see how much it can be simplified and pared down so that each shape perhaps doesn’t need its own series of size conditionals, etc.  

Again, I’ve found this week’s work to be fairly straightforward, so I’ve not much more to write.  But, I’m excited to see everything coming together.  And I’m now starting to see the real potential of Python when it comes to cleaning, parsing, and transforming data; and then going further with it to create visual representations of it.  
