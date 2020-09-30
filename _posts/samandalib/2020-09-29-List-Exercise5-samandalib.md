---
layout: post
author: samandalib
title: "List Exercise number 5"
---
<iframe src="https://trinket.io/embed/python/edb70ad1ee" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---
Reflection
---
This exercise seems a little complicated at first but since the output sample is provided, it is clear what I was trying to achieve. The only thing that took a little time to realize
for me was to understand how to skip lines that do not start with `from`. I did it with a single line of code:
```python
  if line.startswith("From"):
  ```
In this way if a line starts with "From", I will get the name after it but if it doesn't, I will just skip it. At the end by using the formatting that I learned form string section, 
I showed the total number of names found.
It was a cool brain exercise.
