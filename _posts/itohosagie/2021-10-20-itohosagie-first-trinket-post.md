---
layout: post
author: itohosagie
title: "Itohan's First Trinket Post"
---

For my first Trinket post I wanted to share an example from our textbook that went over tuples, as this was a concept that I initially struggled with. Within this exmple we're asked to sort a dictionary and recall its items by sorting by the value in reverse order. 

Here's the full code I've written here:

<iframe src="https://trinket.io/embed/python/8552a0758c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

After the dictionary was defined and an empty list was created to capture the final sorted list, I tried to construct a list based on the items within the dictionary provided. To do this I utilized a `for` loop, in which the value and key from the items were appended into the following list: `tup_list`.

```
for (key, value) in d.items():
    tup_list.append((value, key))
```

Following this, I attempted to sort the items within the list by descending order, however the resulting list printed the items with the keys and values swapped, when the intention was to have them just be sorted by the value, without swapping it with the key.

I attempted to use `lambda` to correct this, but unfortunately could not recall the correct method of using the lambda key within this scenario.

```
tup_list = sorted(tup_list, key=lambda x: x[0], reverse=True)
```

Prior to this, I attempted to resolve the issue of reordering the key and value with the following line, but I still ended up with the same result.

```
tup_list.sort(key=lambda x: x[0], reverse=True)
```
Despite multiple attempts at sorting and rearranging the order of the `key` and `value` within each item, I've found myself at a loss. Thankfully, the aspect of deriving a tuple from a dictionary is something that I'm able to grasp, but I'm still stumped as to how `lambda` can be used to resolve this issue, or if there's another option outside of `lambda` that can be used in this instance.
