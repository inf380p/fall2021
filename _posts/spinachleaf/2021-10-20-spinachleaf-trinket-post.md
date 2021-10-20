---
layout: post
author: spinachleaf
title: "spinachleaf's Trinket post"
---
Here's the program I'm embedding:
<iframe src="https://trinket.io/embed/python/e051c2a288" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


This code checks if a string begins with a word character.
```python
import re
def text_match(text):
    pattern = '^[A-Za-z].+'
```
This code returns `Found a match!` if it does, and `Not matched!` if it does not.
```python
 if re.search(pattern, text):
        return("Found a match!")
    else:
        return("Not matched!")
```

When I ran "The quick brown fox jumps over the lazy dog" I got the result `Found a match!` and when I ran "2 foxes jump over lazy dogs" I got the result `Not matched!`
