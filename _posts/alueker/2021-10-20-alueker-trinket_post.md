---
layout: post
author: alueker
title: "Andrew L's Trinket Post"
---
Here is a basic string tester:
<iframe src="https://trinket.io/embed/python/5eb23967dc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```python
import re
def text_match(string):
    pattern = '^[A-Z]' # Your regex pattern here
    if re.search(pattern,  string):
        return("Found a match!")
    else:
        return("Not matched!")
print(text_match("The quick brown fox jumps over the lazy dog."))
```  

This is meant to test whether an entry is a string or not. 
The simpelest way to do so is to see if a line begins (^) with a capital letter [A-Z]
    
A small issue could be if someone has incorrect syntax and chooses to begin a string with a lowercase letter    
