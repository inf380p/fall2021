---
layout: post
author: lulomax
title: "Lucius trinket post"
---

An example using regex:

<iframe src="https://trinket.io/embed/python/fa98d1d34b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Trying to understand regex syntax.
```python

def text_match(text):
    pattern = '[A-Z]_[a-z]+'
```
This was the simplest
```python
    if re.search(pattern, text):
            return('Found a match!')
    else:
            return('Not matched!')
```
