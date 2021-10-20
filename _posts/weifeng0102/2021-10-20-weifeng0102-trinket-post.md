---
layout: post
author: weifeng0102
title: "weifeng0102's trinket post"
---

Here is an example about dictionary:
<iframe src="https://trinket.io/embed/python/e93c16b543" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


It's a write code question on Runestone which cost me much time to write the correct answer.


The question is：
Write a program to record in the dictionary `message_count` the total number of messages from each domain name (not the whole address, just the part after the @ and before the space). At the end of the program, print out the contents of your dictionary. The domains should be the keys of the dictionary, and the counts of the domains should be the values of the dictionary. For example, `message_count['iupui.edu']` should be `8`.

The content of file `mbox-short.txt2` is as follows:
```
gopal.ramasammycook@gmail.com 1
louis@media.berkeley.edu 3
cwen@iupui.edu 5
antranig@caret.cam.ac.uk 1
rjlowe@iupui.edu 2
gsilver@umich.edu 3
david.horwitz@uct.ac.za 4
wagnermr@iupui.edu 1
zqian@umich.edu 4
stephen.marquard@uct.ac.za 2
ray@media.berkeley.edu 1
```
my answer is:

```python
with open("mbox-short.txt2", "r") as filename:
    message_count = {}
    messages = filename.readlines()
    for message in messages:
        email = message.split()[0]
        key = email.split("@")[1]
        value = message.split()[1]
        value = int(value)
        if key not in message_count.keys():
            message_count[key] = value
        else:
            message_count[key] += value
for key in message_count:
    message_count[key] = str(message_count[key])
print(message_count)
```



