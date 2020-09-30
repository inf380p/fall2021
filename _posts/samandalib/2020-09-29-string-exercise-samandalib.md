---
layout: post
author: samandalib
title: "String Exercise"
---

<iframe src="https://trinket.io/embed/python/c3b2591e16" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Reflection:
It was a really short and easy problem to solve. By reading the string part it can be easily coded with few lines of code:
```python
str = 'X-DSPAM-Confidence:0.8475'

#find the index of colon
ind = str.find(":")

#slice the string from the character after colon to the end
number = float(str[ind+1:])

print number
```
