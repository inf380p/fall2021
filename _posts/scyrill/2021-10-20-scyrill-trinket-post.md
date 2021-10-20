---
layout: post
author: scyrill
title: "Scyrill's First Post!"
---
Here is an example about sorting items in a dictionary: 

<iframe src="https://trinket.io/embed/python/42dbe41674" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

When I encountered this problem the first time, it was tricky and I actually gave up for a while because it felt like the answer was outside of what I knew. However, after talking it out with a friend, I got to see how a problem like this would be solved. 

This code begins wiith defining the dictionary keys and values:

```python
d = {'a': 10, 'b': 2, 'c': 27, 'd': 15, 'e': 30, 'f': 3}
```

Following this, I created a list for the tuples called `tup_list` and defined it as being the list of the items in the dictionary, `d`.

```python
tup_list = list(d.items())
```

Afterwards, I created a new list that the keys and values could be sorted into. They were added to the list with the values, `v`, first and the keys, `k`, last. In the following line, the `lst` was sorted so that it was arranged in descending order. 

```python
lst = []
for k, v in d.items():
    lst.append((v, k))
lst.sort(reverse=True)
```

However, this doesn't fully solve the problem as it would end with the incorrect output, in which it would return something like `[30, 'e']` when you want `['e', 30]`. To solve this, you would redefine `tup_list` from earlier, making it empty and then entering `k` and `v` in the correct order in the code. 

```python
tup_list = []
for k, v in lst:
    tup_list.append((v, k))
print(tup_list)

```

After doing it this way, the question was very easy and it made sense!

