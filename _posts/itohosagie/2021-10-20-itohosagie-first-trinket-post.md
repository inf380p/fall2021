---
layout: post
author: itohosagie
title: "Itohan's First Trinket Post"
---

While reviewing tuples from our textbook I came across this example of sorting a dictionary and recalling its items by sorting by the value in reverse order. Here's the full code I've written here:

<iframe src="https://trinket.io/embed/python/8552a0758c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

To capture a list based on the items within the dictionary provided I utilized a `for` loop, in which the value and key from the items were appended into the following list: `tup_list`:

```
for (key, value) in d.items():
    tup_list.append((value, key))
```

Following this, I attempted to sort the items within the list by descending order, however the resulting list prints the items with the keys and values swapped, when the intention was to have them just be sorted by the value, without swapping it with the key.

I've attempted to use `lambda` to correct this, but am afraid that I've forgetten the correct syntax ...

```
tup_list = sorted(tup_list, key=lambda x: x[0], reverse=True)
```

I understand the method of deriving a tuple from a dictionary, but in this scenario I'm still a little stumped as to how `lambda` can be used to resolve this print issue.
