---
layout: post
author: cridley17
title: "Claire's Trinket Post"
---
Here is an example of using regex to search within strings:

<iframe src="https://trinket.io/embed/python/7ff9eb4058" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code defines a function `match_cat()` that will display true for any string that contains the letters 'cat' in any case. 

```
def match_cat(strings):
    word = '[cC]+[aA]+[tT]'
```

The code then uses a condition to search a string. If the letters match any case of the letters in 'cat' the function returns True, if not it returns false. 
```
    if re.search (word, strings):
        return True
    else:
        return False
```

When I intially worked on this code in Runestone, I struggled to figure out how to ensure that a mix of upper and lower case letters would return True. 

My first function looked like this:

```
def match_cat(strings):
    word = '[c]+[a]+[t]'
```
This function will only match lowercase letters. 

In order to match uppercase letters and lowercase letters, both need to be included within the brackets like this:

```
word = '[cC]+[aA]+[tT]'
```

One important thing to note is to remember to import regex by starting the code with `import re`. If this is not done the code will not work at all. 
