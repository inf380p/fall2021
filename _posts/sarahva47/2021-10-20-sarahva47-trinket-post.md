---
layout: post
author: sarahva47
title: "Sarah Varenhorst's trinket post."
---

Here's an example of how to use Regex (regular expressions) to make a list. I chose this example because I was pretty confused due to the weird syntax of emails, and couldn't wholly figure it out until we discussed this problem in class, so I'm taking a moment to document my understanding of this problem for future regex use.:

<iframe src="https://trinket.io/embed/python/f945d6ce15" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This problem from chapter 12 takes a file, pulls out all email addresses, and puts them in a list of emails.

This piece of code sets up the problem by first importing the information needed to use regex, then getting the file, and defining the list. This is important to do first so that everything is set up. :

```
import re
hand = open('mbox-short4.txt')
email_list = []
```

The pattern needed to pull out an email is weird, particularly because the syntax of emails requires an "@" and a "." so there are multiple parts. What this is doing is saying that the first character can be any letter (including uppercase or lowercase) followed by some non-whitespace characters (so, the "\S+" parts), then an "@" symbol for the domain, followed by some non-whitespace characters, and ending again with a letter (including uppercase or lowercase) or a number. :

```
pattern = "[A-Za-z0-9]\S+@\S+[A-Za-z0-9]"
```
