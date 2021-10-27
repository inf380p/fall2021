---
layout: post
author: sj-roh
title: "SJ's two trinket post and reflection"
---


# My Trinket from the textbook:

<iframe src="https://trinket.io/embed/python/755b71b955" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

For Trinket 1, I think the biggest thing for me was making sure that I knew which direction, and at what angle each line for the V was headed towards, 
and also making sure that I knew how to only turn the turtle twice while not using penup or pendown. I think the lightbulb moment for me happened when 
I looked through my notes to check how I could move to a specific set of coordinates to start programming the necessary lines to draw. I was confused 
because initially, my mind went through strategies on how I could turn the direction backwards to begin at the starting point (0,0), but I noticed that 
these steps would require turns. 

The geometric command: `.goto()`, was exactly what I was looking for. A function that would allow me to move the turtle position of the next line without 
using any turns, penups, or pen downs. Next, making sure that I added the colors (color 1, color 2) as parameters to be inputted when calling the function, 
was something that I did not do initially. I wanted to make sure that whoever calls this function has the ability to customize it so they could choose whatever 
colors. Making sure these parameters were included was essential. 

# My Trinket I made:

<iframe src="https://trinket.io/embed/python/b11ef55686" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Reflection

For Trinket 2, I think a confusion for me was knowing the structure of how I wanted to code so I would include a function, for loop, and chained conditional 
statements. Then, it was just coming up with my own design that is interesting enough to me. I wanted to still use the shape-based problems that we focused 
on so much during this chapter, but include my own design and twist. A confusion I ran into was not knowing the correct order for filling the shapes with 
colors: setting the turtle color, instantiating the filling of the color, beginning to fill, and ending the fill. I started with writing the `fillcolor()` 
function followed by the `begin_fill()` function, then followed by the `end_fill()` function before the drawing lines of code, and noticed this did not work. 
One important lesson I learned was that the `end_fill()` must come after the program knows what to draw. 

As I ran through my first couple of attempts, I noticed that if this code would only make sense to me with some of the language I used. I wanted to make sure 
that the code would make sense to any reader, without any explanation of what I intended to do. I started with verbiage like “range_value” instead of “sides” 
as a parameter, but I realized that it would not be intuitive to someone running the code. Thus, I made the change throughout the code and this small change 
made a huge difference (i.e, 360/num_sides vs. 360/range_value, makes more sense). 
