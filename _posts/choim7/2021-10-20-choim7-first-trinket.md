---
layout: post
author: choim7
title: "Moonjeog's trinket post"
---

Here's the example about list reversing:

<iframe src="https://trinket.io/embed/python/d1e4b9f98b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code defines a function that is used as the reserve sorting in the call lst.revserse():

```
def reverse(lst):
    lst.reverse()
    return lst
    #return lst[-1::-1]
    
print(reverse([1,2,3]))
```

This is the same result as using lst[-1::-1]

