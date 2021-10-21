---
layout: post
author: srj1220
title: "Sarah James's trinket post"
---

Here's a code that uses regex:

```
import re
def text_match(text):
    pattern = '^[A-Za-z]+'
    if re.search(pattern, text):
        return("Found a match!")
    else:
        return("Not matched!")
print(text_match("The quick brown fox jumps over the lazy dog."))
```
<iframe src="https://trinket.io/embed/python/5150252c53" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

This isn't the most complex code by any means, but I was very happy with it at the time, since I felt confident writing the regex for it. At first I had had a rough time understanding how to write the patterns, but after a bit of trial and error I was able to get it to do what I wanted it to.
Regex can easily be used to find more complex patterns such as `"[a-zA-Z0-9]\S+@\S+[a-zA-Z]"` in the code below:

```
import re
hand = open('mbox-short4.txt')
email_list = []
for line in hand:
    line = line.rstrip()
    emails = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z]", line)
    for email in emails:
        email_list.append(emails)
print(email_list)
```
