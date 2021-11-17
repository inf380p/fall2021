---
layout: post
author: tommytestertwo
title: "Tommy's trinket post"
---

For my first trinket post, here's an example about lambdas and sorting:

<iframe src="https://trinket.io/embed/python/e07cd1c4ed" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code defines a function that is then used as the sort key in the call to `item.sort()`:

```python
def get_first_item(x):
  return x[0]

items.sort(key = get_first_item)
```

This is the same result as using a lambda like this:

```python
items.sort(key = lambda x: x[0])
```

In this case, a lambda is more efficient to write if the function won't be reused. The named function `get_first_item` might be a good way to write this program if there were recurring need to sort by the first item of a sequence.

Overall, lambdas can be useful, but they're very terse and only impact one portion of the code.
