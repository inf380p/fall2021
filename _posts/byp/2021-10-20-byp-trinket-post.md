---
layout: post
author: byp
title: byp's trinket post!"
---

Here's an example about regex :

<iframe src="https://trinket.io/embed/python/f3f9f9a9cf" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


```python
import re
s = ['X-DSPAM-Confidence: 0.8475', 'X-DSPAM-Probability: 0.0000', 'X-DSPAM-Confidence: 0.6178', 'X-DSPAM-Probability: 0.0000']
for item in s:
    x = re.findall('^X\S*: ([0-9.]+)', item)
    if len(x) > 0:
        print(x)
```

when you are using `findall()`, parentheses indicate that while you want the whole expression to match, you only are interested in extracting a portion of the substring that matches the regular expression.

Instead of calling `search()`, we add parentheses around the part of the regular expression that represents the floating-point number to indicate we only want `findall()` to give us back the floating-point number portion of the matching string.
