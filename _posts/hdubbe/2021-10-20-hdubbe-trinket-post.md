---
layout: post
author: hdubbe
title: "Hannah's Trinket Post"
---

Here's an example about searching in a dictionary for words in a particular phrase:

<iframe src="https://trinket.io/embed/python/b907f52ea6" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

When I first attempted this code I made the error of writing a program that searched for and made a list of each individual letter like this:
```
for word in words:
        if word not in word_dictionary.keys():
            word_dictionary[word] = 0
            word_dictionary[word] += 1
        else:
            word_dictionary[word] += 1
```
I corrected this error by revising my code to just make a count of each word in the phrase, rather than the letter. I had to simplify the program in order to this:

```
for word in words:
    if word not in word_dictionary.keys():
        word_dictionary[word] = 0
    if word in word_dictionary.keys(): 
        word_dictionary[word] += 1
```
Then I was able to get the result that I wanted.

          
