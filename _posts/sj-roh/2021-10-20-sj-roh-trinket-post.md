---
layout: post
author: sj-roh
title: "sj-roh's trinket post"
---

Here's an example about using regular expressions with regards to opening a .txt file to search and extract from.

<iframe src="https://trinket.io/embed/python/234a9ca556" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

First, I import the Regular Expressions package library to be able to use all the tools necessary. Then I set the variable `hand` equal to opening 
the .txt file at hand. I set the variable domains equal to an open list to later append the email address domains.

```python
import re
hand = open('mbox-short4.txt')
domains = []
```
Next, I create a for loop, to go through each line in the .txt file to first have the line variable equal to each line without trailing characters at 
the end of a the last string. Then I set `x` equal to my regular expression, searching and extracting the subsets of a string that starts with an 
`@` symbol, followed by one or more non-whitespace characters, ending with a letter from each line.

```python
for line in hand:
    line = line.rstrip()
    x = re.findall('@\S+[a-z]',line)
```
Lastly, I run another for loop to go through the results from the regular expression, and then append each line of domain
to the 'domains' open list. I must call the first element within the returned values for `x` because each line is already 
in a list, and the `findall()` function automatically returns values in a list as well. Thus, I call the first element to
append each domain to the domains list so it contains strings and not lists.

```python
    for domain in x:
        domains.append(x[0])
print(domains)
```
That's it! :D

