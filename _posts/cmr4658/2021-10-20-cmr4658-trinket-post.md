---
layout: post
author: cmr4658
title: "Chase's Trinket Post"
---

Here's an example about using regex to parse through some email data:

<iframe src="https://trinket.io/embed/python/0e425ec584" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

This code opens the file `mbox-short.txt` so the program can read through the lines:

```python
hand = open('mbox-short4.txt')
```

Next, the program goes through each line in the file, finds each email address in the line using a regex expression, and pulls out the number after that email address (representing how many emails were sent from that address).
Finally, it adds up all the numbers in the line and adds the total to the accumulator variable `total-emails`.

```python
for line in hand:
    line_emails = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s?(\d)', line)
    for num in line_emails:
        total_emails += int(num)
```

The regex expression looks complicated, but is easier to understand when breaking it down:

```[a-zA-Z0-9]\S+@\S+[a-zA-Z]\s?(\d)```

It finds all the emails in each line by looking for a sequence of text...

`[a-zA-Z0-9]` That starts with an uppercase/lowercase letter or digit, followed by...

`\S+` One or more non-space characters, followed by...

`@` An at symbol, followed by...

`\S+` One or more non-space characters (again), followed by...

`[a-zA-Z]` An uppercase or lowercase letter, followed by...

`\s?` One or more spaces, followed by...

`(\d)` A digit! Since this is what we need, I used the parentheses to pull it out and use it.
Now I'm editing the post.
