---
layout: post
author: boyeonpark
title: "Boyeon Park's final project update(11/23)."
---


# Revised plan & what I have done

- [O] cleansing data to use (11/16)
  
- [O] designing user interface (11/16)
  
- [O] making two drafts, one for structure, one for sketch (11/16)
  
- [O] considering how to store and retrieve data (11/16)
  
- [O] structuring main loop (11/16)
  
- [O] customizing functions except for drawing a graph (11/16)
  
- [O] import the whole data and see if there are any unexpected errors(11/16)
  
- [O] making a function to format numbers (thousand unit comma) (11/23)
  
- [O] getting to know how to make a graph(matplotlib, pygal, bokeh) (11/23)
  
- [O] deciding which graphical module to use => matpotlib (11/23)
  
- [O] coding for making a graph (11/23)
  
- [O] coding for using a custom module (11/23)
  
- [O] evolving the sketch with what I learned from the class (11/23) - added
  
- [  ] combining main structure code and sketch code (11/30)
  
- [  ] revising codes and comments to be readable (11/30)
  
- [  ] testing and making bug free (12/3)
  
- [  ] writing reflection (12/8)
  

# code for getting to know how to draw a graph
About getting to know how to make a graph(matplotlib, pygal, bokeh):
I searched how to draw a graph in Python using matplotlib, pygal, bokeh and practiced like a code below.
<iframe src="https://trinket.io/embed/python3/dca776a318" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# main structure code that I added making a graph function, custom module ,etc since last week
<iframe src="https://trinket.io/embed/python3/e60cc0908d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# upgraded sketch code 
<iframe src="https://trinket.io/embed/python3/b01a279ca6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
And then I decided to use matplotlib because it is the simplest one. 

# Reflection

About making a custom module: 
At first, I was about to transfer all the functions in main code to the custom module, but there was an error occurred related to a global variable, dictionary.
I was using a dictionary global variable in functions and after they moved to custom module, they couldn’t find this dictionary variable which was in the main code.
And then, I searched on Google about this and found out I can also import a variable when I use custom module.
So created another custom module for global variable and file reading and storing data into dictionary and then, 
I imported the global variable in the custom module for functions. Finally it worked as I intended.
