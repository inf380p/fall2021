---
layout: post
author: boyeonpark
title: "Boyeon Park's final project update(11/30)."
---


# Revised plan & what I have done
  
 - [x] cleansing data to use (11/16)  
 - [x] designing user interface (11/16)
 - [x] making two drafts, one for structure, one for sketch (11/16) 
 - [x] considering how to store and retrieve data (11/16) 
 - [x] structuring main loop (11/16) 
 - [x] customizing functions except for drawing a graph (11/16) 
 - [x] import the whole data and see if there are any unexpected errors(11/16) 
 - [x] making a function to format numbers (thousand unit comma) (11/23)
 - [x] getting to know how to make a graph(matplotlib, pygal, bokeh) (11/23) 
 - [x] deciding which graphical module to use => matpotlib (11/23)
 - [x] coding for making a graph (11/23) 
 - [x] coding for using a custom module (11/23) 
 - [x] evolving the sketch with what I learned from the class (11/23) 
 - [x] combining main structure code and sketch code (11/30) 
 - [x] revising codes and comments to be readable (11/30) 
 - [x] edit data structure to dictionary of dictionary (11/30) - added
 - [ ] testing and making bug free (12/3) 
 - [ ] writing reflection (12/8) 

# the code so far
<iframe src="https://trinket.io/embed/python3/f6b4e05d39" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>  
  
# Reflection
When I was merging the main structure code with the sketch code, I ran in to unexpected ‘list out of range’ errors. 
In the main structure code, I was calling functions directly like `option(2011)` and in the sketch code, I was calling functions with parameter that users enter.
So when I select option1 and enter ‘2011’ it should have been the same as calling directly `option(2011)` but only calling with input parameter had errors, 
so in the function I printed line by line to see where the problem was like `print(1)`, `print(2)`, … `print(6)`. After running and seeing the printing words, 
I found out that I forgot to convert users’ input to integer. Printing is always great thing to do in the first place when we have unexpected errors. 

After adding some comments and editing codes more readable, I had spare time to do some more so I decided to change my data structure from a dictionary 
with tuple keys to a dictionary of dictionary type (for example: {(‘Canada’,2010):1111, ……) -> {‘Canada’: {2010: 1111, 2011: 1111, ….}}
although it wasn’t in a list of plan. Because whenever I coded with the one with tuple keys, I felt that there could be a smarter way. 
After changing to a dictionary of dictionary, I thought this is much better especially for the case of searching data with a specific country. 
It became much simpler like below. 

(before – a dictionary with a tuple key) 
```python
lst = list(dict_a.keys()) # putting the dictionary keys into a list
  result = []# a list to put the result
for key in lst:
    if key[0] == country :
      result.append((key[1],dict_a.get(key)))
```

(after – a dictionary with dictionary)
```python
result = [] # a list to put the result
   result = list(dict_a[country].items())
```
