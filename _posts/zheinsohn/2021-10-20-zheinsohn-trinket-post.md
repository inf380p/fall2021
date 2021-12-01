---
layout: post
author: zheinsohn
title: "Zheinsohn Trinket Post"
---

Regex example:
<iframe src="https://trinket.io/embed/python/f09b7f94fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code uses a regex equation and `re.findall` to extract the number of emails sent from all email addresses.

```python
x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s?(\d)', line)
```

This regex equation iterates through each line of a provided text file of email addresses to extract the number next to each address that indicates the number of emails that each address has sent. The characters in parentheses allow Python to find specific constructions of character in the lines of the text file that match the ranges of characters requested, like the @ symbol here:

```python
\S+@\S+
```
This entire regex expression instructs Python to look for lines in the document that have an @ symbol between alphabetical or numerical characters and ends with a digit, which indicates that the line is an email address followed by a number (of emails sent). This method of extracting a digit from multiple lines of text is more efficient than creating a list and determining where to slice each line to extract the number individually.

```python
 for email in x:
        total_emails += int(email)
```
To calculate the total number of emails sent, we can use this for expression to add all digits extracted.

I selected this piece of code because regex expressions feel like both a fun puzzle and also a great way to visualize how Python iterates and how coding changes the way Python behaves. This was also an example that I discussed in a small group during class after understanding the regex expression but being unsuccessful in getting the for loop to count correctly, and talking with others about my regex expression and the for loop was a fun exchange of knowledge.
