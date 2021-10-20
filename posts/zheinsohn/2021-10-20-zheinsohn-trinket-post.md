---
layout: post
author: Zheinsohn
title: "Zheinsohn Trinket Post"
---

Regex example:
<iframe src="https://trinket.io/embed/python/f09b7f94fd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code uses a regex equation and `re.findall` to extract the number of emails sent from an email address.

```python
x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s?(\d)', line)
```

This regex equation iterates through each line of a provided text file of email addresses to extract the number next to each address that indicates the number of emails that each address has sent. The characters in parentheses allow Python to find specific constructions of character in the lines of the text file that match the ranges of characters requested. This is a more effective way of extracting the number of emails than line slicing.

```python
 for email in x:
        total_emails += int(email)
```
