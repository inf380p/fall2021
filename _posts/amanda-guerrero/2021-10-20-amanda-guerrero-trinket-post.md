---
layout: post 
author: amanda-guerrero
title: "Amanda's trinket post"
---
Here's an example about loops:

<iframe src="https://trinket.io/embed/python/8603e3fb89" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


This question asks you to modify the following existing code: 
```python
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)
```

This code traverses through a `for` loop: 

```python
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
```
