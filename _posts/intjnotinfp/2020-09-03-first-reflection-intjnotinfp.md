---
layout: post
author: intjnotinfp
title: "intjnotinfp's first reflection"
---

This module was confidence building but I’m hoping it’s not a false sense of confidence because I can tell how easy the assignments were. I liked doing the assigned readings and working through things alone and not under the pressure to “get” it quickly in class like the circles and turtles exercises last week. It's useful to note that I like learning this stuff individually then bringing questions or concerns to class afterward. Hoonestly, I can't keep up in class when we fly through examples. The readings were interesting, and I like that Dr. Hauser identified why we’re starting with Python (i.e. the easier syntax, usability, and fact that it can be used in many different contexts. Also, in regard to the comments sections in the Chapter 2 Variables Notes, someone who works in tech told me that no one really uses comments with the pound sign – is that because that’s the “advanced” way to do things? I’m finding “commenting things out” to be pretty useful, so I’m going to keep using that feature regardless. I’m feeling optimistic that I can learn this stuff if it’s broken down in small chunks like this. I was really surprised at how good it feels to finally figure some piece of code out, especially after you’ve been struggling with it for a little while. That feeling when you finally “get” something is pretty great. My programmer friends have told me that it never goes away. It’s kind of like a runner’s high.. but better.

I also experienced my first (I think?) instance of doing something wrong but the program still working. Here’s an example of using float incorrectly and it not jamming up/ still giving me what I expected .
```
# Look what I did here:
C = input ("Enter Degrees Celsius:")
float(C)
F = 1.8 *float(C) + 32
float(F)
print ("Degrees Fahrenheit: ", F)
```
The right way to do this was to assign the floating point type to the input on the same line it's defined.
An example of that:
```
# Better Version:
C = float(input ("Enter Degrees Celsius:"))
F = 1.8 *C + 32
print ("Degrees Fahrenheit: ", F)
```

Overall, great first week!
