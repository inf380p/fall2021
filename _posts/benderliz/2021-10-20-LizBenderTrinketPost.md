---
layout: post
author: benderliz
title: "Liz's Trinket Post"
---

Here is my example that uses a dictionary as a counter:

<iframe src="https://trinket.io/embed/python/b129d32d14" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code creates an empty dictionary to store words from a given phrase, and then splits the phrase to be stored into individual words:
```
phrase = "Writing programs or programming is a very creative and rewarding activity  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem  This book assumes that {\em everyone} needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills"
word_dictionary={}
words = phrase.split()
```
The following code then uses a ``for loop`` to iterate through each word, setting it to lowercase.
```
for word in words:
    word = word.lower()
```
Then, the words are stored in the dictionary. We use the ``in operator`` to check that the string is in the dictionary.
```
    if word in word_dictionary:
        word_dictionary[word]+=1
    else:
        word_dictionary[word]=1
print(word_dictionary)
```
Overall, this is a simple example of using a dictionary to count the number of times each word is used in a given phrase. This example was one of the first lightbulb moments I had in class regarding how to iterate through ``for loops`` to count something, and then use dictionaries to store it.

I am practicing making an edit here!
