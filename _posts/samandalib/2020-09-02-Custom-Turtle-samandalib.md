---
layout: post
author: samandalib
title: "Custom Turtle Excercise"
---
<iframe src="https://trinket.io/embed/python/bce9db6e0a" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
This excercise seems to be easy. However, it reminds me how important it is to look for documentations even if I believe something is easy. I had no problem in writing the input statement
also setting the color of the turtle was not a big deal. But changing the background color was different. I expected that the instance of the Turtle that I defined with name "tina" be 
able to change the background color but surprisingly it wasn't the case. I did a couple of tries with tina, but wasn't successful. So I found no way but to go and look for it in the 
documentation. I found that I can only access the Screen method within the "turtle" library and not an instance of the "Turtle" that I defined. It seems that Screen method is a global
one that instances of Turtles have no access to! That was a good thing to know.
