---
layout: post
author: Elizard0926
title: "Elizabeth's Trinket Post"
---

Here's an example about Regex:

<iframe src="https://trinket.io/embed/python/d5a5e3c669" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This example was part of a sequence of exercises that asked the programmer to extract different parts of a given file.
In the problem, it asks to "extract the number next to each email."
Since it wasn't clear where the number was on the line (could've been on the left side or the right side, space or no space between # and email, etc.), my first objective was to read the lines and determine its location (which was a good refresher on how to read files!)

```python
hand = open('mbox-short4.txt','r')
#figure out where the number is
print(hand.readlines())
```
The resulting lines that print show that the number of emails comes after a space at the end of the email:

```python
['gopal.ramasammycook@gmail.com 1\n', 'louis@media.berkeley.edu 3\n', 'cwen@iupui.edu 5\n', 'antranig@caret.cam.ac.uk 1\n', 'rjlowe@iupui.edu 2\n', 'gsilver@umich.edu 3\n', 'david.horwitz@uct.ac.za 4\n', 'wagnermr@iupui.edu 1\n', 'zqian@umich.edu 4\n', 'stephen.marquard@uct.ac.za 2\n', 'ray@media.berkeley.edu 1\n']
```

Buildings off of the previous problems, I put in my regex expression (referred to as "regex equation" in Runestone) and then added in parenetheses to extract the number at the end of the line.

```python
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s([0-9])', line)
```

Where I started to run into problems was when I was trying to take those numbers and append them into the empty list `num_lst` which I created earlier. Here is the correct code:

```python
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s([0-9])', line)
    for numbers in x:
        num_lst.append(numbers) 
print(num_lst)
```
Note what is in in the parentheses in the `.append` line. Instead of `num_list.append(numbers)` I had `num_lst.append(x)`. Instead of taking the numbers it had found, the program appended a list of the emails which looked something like this:

```python
[['gopal.ramasammycook@gmail.com'], ['louis@media.berkeley.edu'], ['cwen@iupui.edu'], ['antranig@caret.cam.ac.uk'], ['rjlowe@iupui.edu'], ['gsilver@umich.edu'], ['david.horwitz@uct.ac.za'], ['wagnermr@iupui.edu'], ['zqian@umich.edu'], ['stephen.marquard@uct.ac.za'], ['ray@media.berkeley.edu']]
```

This was a good reminder that when writing a `for` loop, the loop iterates over the elements (the part that comes directly after the "for") in the sequence (the part that comes after the "in").
