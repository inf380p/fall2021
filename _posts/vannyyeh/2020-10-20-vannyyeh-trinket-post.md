---
layout: post
author: <yourgithubname>
title: " Vanny's trinket post"
---

Here's an example about the list and dictionary:

<iframe src="https://trinket.io/embed/python/d837a76d86" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


This code defines a function that is then used the dictionary and list concept:
```python 
def list_link(lst1, lst2):
    diction = {}
    counter = 0
    if len(lst1) == len(lst2):
        for i in lst1:
            diction[i] = lst2[counter]
            counter += 1
    return diction
    print(diction)
```

This is another code shows the example:

```python 

def add_to_new_list(lst):
    new_list = []
    new_list.append(len(lst))
    new_list.append(lst[0] * 3)
    return new_list

```

    
End, hope the readers understand examples...
