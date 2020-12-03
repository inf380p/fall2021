---
author: EAkita
layout: post
title: "Class_Extensions Hack!"
---

The embedded link is below: 

<iframe src="https://trinket.io/embed/python/1856305293" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


**Reflection**
The most difficult part about this assignment was figuring out how to properly setup class extensions and pass on created methods to other functions within the class. I had some difficulty with the user input section. I had to create a col_update() function to update the individual items in the list (shown in the code snippet below). I thus ran the program twice, once using the default colors I set, and a second to test the user input for creating the spirograph, as passed between the functions for the extended turtle Akita class. 


```python
def col_update(self):
      col1 = input("Enter new color 1: ") #let the user enter to update color
      #update the color list, since spirograph takes from color list and not col 1. 
      self.colorList[0] = col1
      col2 = input("Enter new color 2: ")
      self.colorList[1] = col2
      col3 = input("Enter new color 3: ")
      self.colorList[2] = col3
```
