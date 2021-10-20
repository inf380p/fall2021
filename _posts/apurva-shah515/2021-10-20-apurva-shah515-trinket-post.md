---
layout: post
author: apurva-shah515
title: "Apurva's Trinket post"
---

For my first Trinket post, here's an example about regular expressions and using the `findall()` method:

<iframe src="https://trinket.io/python/a38d17efb9" width="100%" height="600" frameborder="0" marginwidth="0" allowfullscreen></iframe>

This code opens a file called mbox-short4 which contains a list of email addresses and the number of emails sent from each address, and then loops through the text file to extract the usernames from each email address. 

```python
import re
hand = open('mbox-short4.txt')
usernames = []
for line in hand:
    line = line.rstrip()
    all_usernames = re.findall('.+?(?=@)', line)
    for name in all_usernames:
        usernames.append(name)
print(usernames)
```
Here we are making use of the regular expression, `'.+?(?=@)'`, to isolate the part of the email address that comes before the @ symbol. 
I made use of the non-greedy expression with the `?` syntax so that I did not incorporate any additional text. 

We can also modify the regular expression to extract different information from the text file. For example, to extract the domains from each email address:

```python
import re
hand = open('mbox-short4.txt')
domains = []
for line in hand:
    line = line.rstrip()
    all_domains = re.findall('@\S+[a-zA-Z]', line)
    for domain in all_domains:
        domains.append(domain)
print(domains)
```
Making use of regular expressions for text parsing in this way makes the process much simpler!
