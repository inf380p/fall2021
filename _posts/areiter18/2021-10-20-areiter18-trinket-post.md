---
layout: post
author: areiter18
Title: "Andrew Reiter's Trinket Post"
---
Here's my trinket post:

<iframe src="https://trinket.io/embed/python/ae2636e831" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


 This code finds sequences with one uppercase letter followed by an underscore followed by one or more lowercase letters. I struggeled at first to find the right code to get the desired sequence. 
 
 This part of the code returns a match using the parameters above:

 ```

def text_match(text):
    pattern = '[A-Z]_[a-z]+'
    if re.search(pattern,  text):
        return('Found a match!')
        
```
 
Here are some of the examples I used to test this code:
 
```

print(text_match("aab_cbbbc"))
print(text_match("aBba_CbQuZ"))
print(text_match("A_aaaab"))
print(text_match("Q_c"))

```
